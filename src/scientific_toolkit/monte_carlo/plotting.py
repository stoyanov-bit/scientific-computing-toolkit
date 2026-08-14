from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def plot_pi_estimation(
    x: np.ndarray,
    y: np.ndarray,
    output_path: str,
) -> None:
    Path(output_path).parent.mkdir(exist_ok=True)

    inside = x**2 + y**2 <= 1

    plt.figure()
    plt.scatter(x[inside], y[inside], s=2, label="Inside circle")
    plt.scatter(x[~inside], y[~inside], s=2, label="Outside circle")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Monte Carlo Estimation of Pi")
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_random_walk(
    x: np.ndarray,
    y: np.ndarray,
    output_path: str,
) -> None:
    Path(output_path).parent.mkdir(exist_ok=True)

    plt.figure()
    plt.plot(x, 
             y,
             linewidth=1,
             alpha=0.8,)
    plt.scatter(x[0],
                y[0],
                s=120,
                color="green",
                edgecolors="black",
                label="Start",
                zorder=5
            )
    plt.scatter(x[-1],
                y[-1],
                s=120,
                color="red",
                edgecolors="black",
                label="End",
                zorder=5,
            )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2D Random Walk")
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_brownian_motion(
    x: np.ndarray,
    y: np.ndarray,
    output_path: str,
) -> None:

    Path(output_path).parent.mkdir(exist_ok=True)

    plt.figure()

    plt.plot(
        x,
        y,
        linewidth=1,
        alpha=0.8,
    )

    plt.scatter(
        x[0],
        y[0],
        s=220,
        color="green",
        edgecolors="black",
        label="Start",
        zorder=5,
    )

    plt.scatter(
        x[-1],
        y[-1],
        s=180,
        color="red",
        edgecolors="black",
        label="End",
        zorder=5,
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Brownian Motion")

    plt.axis("equal")

    plt.legend()

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()


def plot_radioactive_decay(
    atoms_remaining: np.ndarray,
    output_path: str,
) -> None:
    Path(output_path).parent.mkdir(exist_ok=True)

    time_steps = np.arange(len(atoms_remaining))

    plt.figure()
    plt.plot(time_steps, atoms_remaining)
    plt.xlabel("Time step")
    plt.ylabel("Atoms remaining")
    plt.title("Monte Carlo Simulation of Radioactive Decay")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_parameter_distribution(
    values: np.ndarray,
    parameter_name: str,
    output_path: str,
) -> None:

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.figure()

    plt.hist(
        values,
        bins=30,
    )

    plt.xlabel(parameter_name)
    plt.ylabel("Count")
    plt.title(
        f"Monte Carlo Distribution: "
        f"{parameter_name}"
    )

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()