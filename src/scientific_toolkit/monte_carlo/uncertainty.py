import numpy as np


def monte_carlo_fit_uncertainty(
    model,
    fit_function,
    x: np.ndarray,
    y: np.ndarray,
    initial_guess: list[float],
    noise_std: float,
    n_simulations: int = 500,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    rng = np.random.default_rng(seed)

    parameter_results = []

    for _ in range(n_simulations):

        noise = rng.normal(
            loc=0.0,
            scale=noise_std,
            size=len(y),
        )

        simulated_y = y + noise

        try:
            parameters, _ = fit_function(
                model=model,
                x=x,
                y=simulated_y,
                initial_guess=initial_guess,
            )

            parameter_results.append(parameters)

        except (RuntimeError, ValueError):
            continue

    if not parameter_results:
        raise RuntimeError(
            "All Monte Carlo fits failed."
        )

    parameter_results = np.array(
        parameter_results
    )

    parameter_means = np.mean(
        parameter_results,
        axis=0,
    )

    parameter_stds = np.std(
        parameter_results,
        axis=0,
        ddof=1,
    )

    return (
        parameter_means,
        parameter_stds,
        parameter_results,
    )