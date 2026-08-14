import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def generate_signal(
        frequency:float,
        sampling_rate:float,
        duration:float,
        noise_level:float = 0.0,
) -> tuple[np.ndarray,np.ndarray]:
    t=np.arange(0, duration, 1/sampling_rate)
    signal = np.sin(2*np.pi*frequency*t)

    if noise_level>0:
        signal+=noise_level*np.random.randn(len(t))

    return t, signal

def compute_fft(
        signal:np.ndarray,
        sampling_rate: float,
) -> tuple[np.ndarray,np.ndarray]:
    n=len(signal)
    frequencies = np.fft.rfftfreq(n, d=1/sampling_rate)
    spectrum = np.abs(np.fft.rfft(signal))/n

    return frequencies, spectrum

def find_dominant_frequency(
        frequencies:np.ndarray,
        spectrum:np.ndarray,
) ->float:
    peak_index = np.argmax(spectrum)
    return float(frequencies[peak_index])

def detect_spectrum_peaks(
    frequencies: np.ndarray,
    spectrum: np.ndarray,
    min_height_ratio: float = 0.2,
) -> list[float]:
    min_height = np.max(spectrum) * min_height_ratio

    peaks, _ = find_peaks(
        spectrum,
        height=min_height,
    )

    return [float(frequencies[p]) for p in peaks]

def plot_signal(
        time:np.ndarray,
        signal:np.ndarray,
        output_path:str,
) -> None:
    plt.figure()
    plt.plot(time,signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Time Signal")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_spectrum(
        frequencies:np.ndarray,
        spectrum:np.ndarray,
        output_path: str,
) ->None:
    plt.figure()
    plt.plot(frequencies,spectrum)
    plt.xlabel("Frequency [s]")
    plt.ylabel("Amplitude")
    plt.title("Frequency Spectrum")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()