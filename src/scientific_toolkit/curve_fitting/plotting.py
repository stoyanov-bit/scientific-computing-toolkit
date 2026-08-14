from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot_fit(
    x: np.ndarray,
    y: np.ndarray,
    y_fit: np.ndarray,
    output_path: str,
    model_name: str,
    parameter_names: str,
    parameters: np.ndarray,
    parameter_errors: np.ndarray,
    r_squared: np.ndarray,
) -> None:
    Path(output_path).parent.mkdir(exist_ok=True)

    plt.figure()
    plt.scatter(x, y, s=12, label="Data")
    plt.plot(x, y_fit, label="Fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Curve Fit")
    plt.legend()

    parameter_text = f"{model_name} Fit\n\n"

    for name, value, error in zip(parameter_names, parameters, parameter_errors):
        parameter_text += f"{name}: {value:.3f}± {error:.3f}\n"

    parameter_text += f"\nR² = {r_squared:.4f}"
    plt.text(
        0.02,
        0.98,
        parameter_text,
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(
            boxstyle="round",
            facecolor="white",
            alpha=0.85,
        ),
    ) 
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()