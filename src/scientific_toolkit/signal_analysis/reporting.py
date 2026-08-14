from pathlib import Path


def save_analysis_report(
    output_path: str,
    filename: str,
    samples: int,
    sampling_rate: float,
    dominant_frequency: float,
    detected_peaks: list[float],
    statistics: dict[str, float],
) -> None:
    report_path = Path(output_path)

    with report_path.open("w", encoding="utf-8") as file:
        file.write("Signal Analysis Report\n")
        file.write("======================\n\n")

        file.write(f"File: {filename}\n")
        file.write(f"Samples: {samples}\n")
        file.write(f"Sampling rate: {sampling_rate:.2f} Hz\n")
        file.write(f"Dominant frequency: {dominant_frequency:.2f} Hz\n\n")

        file.write("Detected peaks:\n")
        for peak in detected_peaks:
            file.write(f"- {peak:.2f} Hz\n")

        file.write("\nSignal statistics:\n")
        for key, value in statistics.items():
            file.write(f"{key}: {value:.4f}\n")