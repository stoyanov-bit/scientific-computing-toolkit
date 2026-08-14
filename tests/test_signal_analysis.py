import numpy as np

from scientific_toolkit.signal_analysis.spectrum import (
    compute_fft,
    find_dominant_frequency,
    detect_spectrum_peaks,
)

from scientific_toolkit.signal_analysis.metrics import (
    compute_signal_statistics,
)


def test_fft_detects_frequency():
    sampling_rate = 1000
    frequency = 50
    duration = 1.0

    time = np.arange(
        0,
        duration,
        1 / sampling_rate,
    )

    signal = np.sin(
        2 * np.pi * frequency * time
    )

    frequencies, spectrum = compute_fft(
        signal,
        sampling_rate,
    )

    dominant_frequency = find_dominant_frequency(
        frequencies,
        spectrum,
    )

    assert np.isclose(
        dominant_frequency,
        frequency,
        atol=1.0,
    )


def test_peak_detection():
    sampling_rate = 1000
    duration = 1.0

    time = np.arange(
        0,
        duration,
        1 / sampling_rate,
    )

    signal = (
        np.sin(2 * np.pi * 50 * time)
        + 0.5 * np.sin(2 * np.pi * 120 * time)
    )

    frequencies, spectrum = compute_fft(
        signal,
        sampling_rate,
    )

    peaks = detect_spectrum_peaks(
        frequencies,
        spectrum,
    )

    assert any(
        np.isclose(peak, 50, atol=1.0)
        for peak in peaks
    )

    assert any(
        np.isclose(peak, 120, atol=1.0)
        for peak in peaks
    )


def test_signal_statistics():
    signal = np.array(
        [1.0, 2.0, 3.0, 4.0, 5.0]
    )

    statistics = compute_signal_statistics(signal)

    assert np.isclose(
        statistics["mean"],
        3.0,
    )

    assert np.isclose(
        statistics["min"],
        1.0,
    )

    assert np.isclose(
        statistics["max"],
        5.0,
    )