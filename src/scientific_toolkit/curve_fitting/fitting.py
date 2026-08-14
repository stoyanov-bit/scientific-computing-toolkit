from typing import Callable
import numpy as np
from scipy.optimize import curve_fit


def fit_model(
    model: Callable,
    x: np.ndarray,
    y: np.ndarray,
    initial_guess: list[float],
) -> tuple[np.ndarray, np.ndarray]:
    parameters, covariance = curve_fit(
        model,
        x,
        y,
        p0=initial_guess,
        maxfev=10000,
    )

    return parameters, covariance


def compute_r_squared(
    y: np.ndarray,
    y_fit: np.ndarray,
) -> float:
    residuals = y - y_fit
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    return float(1 - ss_res / ss_tot)