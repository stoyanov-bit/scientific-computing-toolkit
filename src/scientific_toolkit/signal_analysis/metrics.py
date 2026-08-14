import numpy as np


def compute_signal_statistics(signal: np.ndarray) -> dict[str, float]:
    return {
        "mean": float(np.mean(signal)),
        "std": float(np.std(signal)),
        "rms": float(np.sqrt(np.mean(signal**2))),
        "min": float(np.min(signal)),
        "max": float(np.max(signal)),
    }