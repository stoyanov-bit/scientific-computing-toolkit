import numpy as np


def linear(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return a * x + b


def exponential_decay(
    x: np.ndarray,
    amplitude: float,
    decay_rate: float,
    offset: float,
) -> np.ndarray:
    return amplitude * np.exp(-decay_rate * x) + offset


def gaussian(
    x: np.ndarray,
    amplitude: float,
    center: float,
    sigma: float,
    offset: float,
) -> np.ndarray:
    return amplitude * np.exp(-((x - center) ** 2) / (2 * sigma**2)) + offset


def sine(
    x: np.ndarray,
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
) -> np.ndarray:
    return amplitude * np.sin(2 * np.pi * frequency * x + phase) + offset