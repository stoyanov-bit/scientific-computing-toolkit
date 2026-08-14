import numpy as np

from scientific_toolkit.curve_fitting.models import (
    linear,
    sine,
)

from scientific_toolkit.curve_fitting.fitting import (
    fit_model,
    compute_r_squared,
)


def test_linear_fit():
    x = np.linspace(
        0,
        10,
        100,
    )

    y = 2.0 * x + 3.0

    parameters, covariance = fit_model(
        model=linear,
        x=x,
        y=y,
        initial_guess=[1.0, 1.0],
    )

    slope = parameters[0]
    intercept = parameters[1]

    assert np.isclose(
        slope,
        2.0,
        atol=0.01,
    )

    assert np.isclose(
        intercept,
        3.0,
        atol=0.01,
    )


def test_sine_fit():
    x = np.linspace(
        0,
        2,
        1000,
    )

    amplitude = 2.0
    frequency = 5.0
    phase = 0.3
    offset = 0.2

    y = sine(
        x,
        amplitude,
        frequency,
        phase,
        offset,
    )

    parameters, covariance = fit_model(
        model=sine,
        x=x,
        y=y,
        initial_guess=[
            1.8,
            5.0,
            0.0,
            0.0,
        ],
    )

    assert np.isclose(
        parameters[0],
        amplitude,
        atol=0.05,
    )

    assert np.isclose(
        parameters[1],
        frequency,
        atol=0.05,
    )


def test_r_squared_perfect_fit():
    y = np.array(
        [1.0, 2.0, 3.0, 4.0]
    )

    y_fit = np.array(
        [1.0, 2.0, 3.0, 4.0]
    )

    r_squared = compute_r_squared(
        y,
        y_fit,
    )

    assert np.isclose(
        r_squared,
        1.0,
    )