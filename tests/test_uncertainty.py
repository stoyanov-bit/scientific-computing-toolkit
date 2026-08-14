import numpy as np

from scientific_toolkit.curve_fitting.models import (
    sine,
)

from scientific_toolkit.curve_fitting.fitting import (
    fit_model,
)

from scientific_toolkit.monte_carlo.uncertainty import (
    monte_carlo_fit_uncertainty,
)


def test_monte_carlo_fit_uncertainty():
    x = np.linspace(
        0,
        2,
        1000,
    )

    true_amplitude = 2.0
    true_frequency = 5.0
    true_phase = 0.2
    true_offset = 0.1

    y = sine(
        x,
        true_amplitude,
        true_frequency,
        true_phase,
        true_offset,
    )

    means, stds, parameter_results = (
        monte_carlo_fit_uncertainty(
            model=sine,
            fit_function=fit_model,
            x=x,
            y=y,
            initial_guess=[
                2.0,
                5.0,
                0.0,
                0.0,
            ],
            noise_std=0.05,
            n_simulations=50,
            seed=42,
        )
    )

    # Four parameters:
    # amplitude, frequency, phase, offset
    assert len(means) == 4
    assert len(stds) == 4

    # Estimated parameters should remain
    # close to the true values
    assert np.isclose(
        means[0],
        true_amplitude,
        atol=0.1,
    )

    assert np.isclose(
        means[1],
        true_frequency,
        atol=0.1,
    )

    # Standard deviations cannot be negative
    assert np.all(stds >= 0)

    # At least one simulation should succeed
    assert len(parameter_results) > 0

    # Every simulation should return
    # four fitted parameters
    assert parameter_results.shape[1] == 4