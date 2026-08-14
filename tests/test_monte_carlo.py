import numpy as np

from scientific_toolkit.monte_carlo.simulations import (
    estimate_pi,
    random_walk_2d,
    brownian_motion,
    radioactive_decay,
)


def test_pi_estimation():
    pi_estimate, x, y = estimate_pi(
        n_points=100_000,
        seed=42,
    )

    assert abs(
        pi_estimate - np.pi
    ) < 0.02

    assert len(x) == 100_000
    assert len(y) == 100_000


def test_random_walk_length():
    n_steps = 100

    x, y = random_walk_2d(
        n_steps=n_steps,
        seed=42,
    )

    assert len(x) == n_steps
    assert len(y) == n_steps


def test_brownian_motion_length():
    n_steps = 500

    x, y = brownian_motion(
        n_steps=n_steps,
        step_std=1.0,
        seed=42,
    )

    assert len(x) == n_steps
    assert len(y) == n_steps


def test_brownian_motion_is_reproducible():
    x1, y1 = brownian_motion(
        n_steps=100,
        seed=42,
    )

    x2, y2 = brownian_motion(
        n_steps=100,
        seed=42,
    )

    assert np.array_equal(x1, x2)
    assert np.array_equal(y1, y2)


def test_radioactive_decay():
    atoms_remaining = radioactive_decay(
        n_atoms=1000,
        decay_probability=0.05,
        n_steps=100,
        seed=42,
    )

    assert atoms_remaining[0] == 1000

    assert np.all(
        np.diff(atoms_remaining) <= 0
    )

    assert atoms_remaining[-1] >= 0