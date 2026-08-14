import numpy as np
from scipy.signal import butter, filtfilt


def bandpass_filter(
    signal: np.ndarray,
    sampling_rate: float,
    lowcut: float,
    highcut: float,
    order: int = 4,
) -> np.ndarray:
    nyquist = 0.5 * sampling_rate

    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype="band")

    return filtfilt(b, a, signal)