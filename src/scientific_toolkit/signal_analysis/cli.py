from pathlib import Path
import numpy as np

from scientific_toolkit.signal_analysis.data_loader import load_signal_csv
from scientific_toolkit.signal_analysis.spectrum import (
    compute_fft,
    find_dominant_frequency,
    detect_spectrum_peaks,
)
from scientific_toolkit.signal_analysis.metrics import compute_signal_statistics
from scientific_toolkit.signal_analysis.filters import bandpass_filter
from scientific_toolkit.signal_analysis.reporting import save_analysis_report

from scientific_toolkit.curve_fitting.models import sine
from scientific_toolkit.curve_fitting.fitting import (
    fit_model,
    compute_r_squared,
)

from scientific_toolkit.monte_carlo.uncertainty import (
    monte_carlo_fit_uncertainty,
)

from scientific_toolkit.monte_carlo.plotting import (
    plot_parameter_distribution,
)


def run_signal_analysis():
    data_folder = Path("data/signal_analysis")
    result_folder = Path("results/signal_analysis")
    result_folder.mkdir(parents=True, exist_ok=True)

    csv_files = list(data_folder.glob("*.csv"))

    if not csv_files:
        print("No CSV files found.")
        return

    print("\nAvailable signal files:")

    for index, file in enumerate(csv_files, start=1):
        print(f"{index}. {file.name}")

    choice = int(input("\nChoose file number: "))
    csv_path = csv_files[choice - 1]

    data = load_signal_csv(str(csv_path))

    time = data.x
    signal = data.y

    dt = time[1] - time[0]
    sampling_rate = 1 / dt

    frequencies, spectrum = compute_fft(
        signal,
        sampling_rate,
    )

    dominant_frequency = find_dominant_frequency(
        frequencies,
        spectrum,
    )

    detected_peaks = detect_spectrum_peaks(
        frequencies,
        spectrum,
    )

    statistics = compute_signal_statistics(signal)

    print(f"\nFile: {csv_path.name}")
    print(f"Sampling rate: {sampling_rate:.2f} Hz")
    print(f"Dominant frequency: {dominant_frequency:.2f} Hz")

    print("\nDetected peaks:")
    for peak in detected_peaks:
        print(f"{peak:.2f} Hz")

    print("\nSignal statistics:")
    for key, value in statistics.items():
        print(f"{key}: {value:.4f}")

    further_analysis = input(
        "\nFit sine model to signal? (y/n): "
    )

    if further_analysis.lower() == "y":
        run_sine_fit(
            time=time,
            signal=signal,
            dominant_frequency=dominant_frequency,
        )

def run_sine_fit(
    time: np.ndarray,
    signal: np.ndarray,
    dominant_frequency: float,
):
    amplitude_guess = (
        np.max(signal) - np.min(signal)
    ) / 2

    offset_guess = np.mean(signal)

    initial_guess = [
        amplitude_guess,
        dominant_frequency,
        0.0,
        offset_guess,
    ]

    parameters, covariance = fit_model(
        model=sine,
        x=time,
        y=signal,
        initial_guess=initial_guess,
    )

    y_fit = sine(time, *parameters)

    r_squared = compute_r_squared(
        signal,
        y_fit,
    )

    parameter_errors = np.sqrt(
        np.diag(covariance)
    )

    parameter_names = [
        "Amplitude",
        "Frequency",
        "Phase",
        "Offset",
    ]

    print("\nSine fit results:")

    for name, value, error in zip(
        parameter_names,
        parameters,
        parameter_errors,
    ):
        print(
            f"{name}: "
            f"{value:.4f} ± {error:.4f}"
        )

    print(f"R²: {r_squared:.4f}")

    run_mc = input(
        "\nRun Monte Carlo uncertainty analysis? (y/n): "
    )

    if run_mc.lower() == "y":

        noise_std = float(
            input(
                "Assumed noise standard deviation: "
            )
        )

        n_simulations_input = input(
            "Number of simulations [500]: "
        )

        if n_simulations_input == "":
            n_simulations = 500
        else:
            n_simulations = int(
                n_simulations_input
            )

        means, stds, parameter_results = (
            monte_carlo_fit_uncertainty(
                model=sine,
                fit_function=fit_model,
                x=time,
                y=signal,
                initial_guess=initial_guess,
                noise_std=noise_std,
                n_simulations=n_simulations,
            )
        )

        print(
            "\nMonte Carlo uncertainty results:"
        )

        for name, mean, std in zip(
            parameter_names,
            means,
            stds,
        ):
            print(
                f"{name}: "
                f"{mean:.4f} ± {std:.4f}"
            )

        result_folder = Path(
            "results/monte_carlo"
            )
        result_folder.mkdir(
            parents=True,
            exist_ok=True,
            )
        for index, name in enumerate(
            parameter_names
            ):
            plot_parameter_distribution(
                parameter_results[:, index],
                parameter_name=name,
                output_path=str(
                    result_folder
                    / f"{name.lower()}_distribution.png"
                    ),
                )