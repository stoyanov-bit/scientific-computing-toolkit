import numpy as np


def estimate_pi(n_points: int, seed: int = 42) -> tuple[float, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)

    x = rng.uniform(-1, 1, n_points)
    y = rng.uniform(-1, 1, n_points)

    inside_circle = x**2 + y**2 <= 1
    pi_estimate = 4 * np.mean(inside_circle)

    return float(pi_estimate), x, y


def random_walk_2d(n_steps: int, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)

    steps = rng.choice([-1, 1], size=(n_steps, 2))
    positions = np.cumsum(steps, axis=0)

    x = positions[:, 0]
    y = positions[:, 1]

    return x, y


def brownian_motion(
    n_steps: int,
    step_std: float = 1.0,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:

    rng = np.random.default_rng(seed)

    dx = rng.normal(0, step_std, n_steps)
    dy = rng.normal(0, step_std, n_steps)

    x = np.cumsum(dx)
    y = np.cumsum(dy)

    return x, y


def radioactive_decay(
    n_atoms: int,
    decay_probability: float,
    n_steps: int,
    seed: int = 42,
) -> np.ndarray:
    rng = np.random.default_rng(seed)

    atoms_remaining = n_atoms
    history = [atoms_remaining]

    for _ in range(n_steps):
        decayed = rng.binomial(atoms_remaining, decay_probability)
        atoms_remaining -= decayed
        history.append(atoms_remaining)

    return np.array(history)