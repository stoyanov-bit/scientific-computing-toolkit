from pathlib import Path

from scientific_toolkit.monte_carlo.simulations import (
    estimate_pi,
    random_walk_2d,
    brownian_motion,
    radioactive_decay,
)

from scientific_toolkit.monte_carlo.plotting import (
    plot_pi_estimation,
    plot_random_walk,
    plot_brownian_motion,
    plot_radioactive_decay,
)

RESULT_FOLDER = Path("results/monte_carlo")
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

def run_monte_carlo():
    print("\nMonte Carlo Demonstrations")
    print("1. Estimate Pi")
    print("2. 2D Random Walk")
    print("3. Brownian Motion")
    print("4. Radioactive Decay")
    print("5. Return")

    choice = input("\nChoose simulation: ")

    if choice == "1":
        run_pi_estimation()

    elif choice == "2":
        run_random_walk()

    elif choice == "3":
        run_brownian_motion()

    elif choice == "4":
        run_radioactive_decay()

    elif choice == "5":
        return

    else:
        print("Invalid choice.")

def run_pi_estimation():
    n_points = int(
        input("Number of random points: ")
    )

    pi_estimate, x, y = estimate_pi(
        n_points=n_points,
    )

    absolute_error = abs(
        pi_estimate - 3.141592653589793
    )

    print(f"\nEstimated Pi: {pi_estimate:.6f}")
    print(f"Absolute error: {absolute_error:.6f}")

    plot_pi_estimation(
        x=x,
        y=y,
        output_path=str(
            RESULT_FOLDER / "pi_estimation.png"
        ),
    )

    print(
        "Plot saved to "
        "results/monte_carlo/pi_estimation.png"
    )

def run_random_walk():
    n_steps = int(
        input("Number of steps: ")
    )

    x, y = random_walk_2d(
        n_steps=n_steps,
    )

    final_distance = (
        x[-1] ** 2 + y[-1] ** 2
    ) ** 0.5

    print(
        f"\nFinal distance from origin: "
        f"{final_distance:.2f}"
    )

    plot_random_walk(
        x=x,
        y=y,
        output_path=str(
            RESULT_FOLDER / "random_walk.png"
        ),
    )

    print(
        "Plot saved to "
        "results/monte_carlo/random_walk.png"
    )

def run_brownian_motion():
    n_steps_input = input(
        "Number of steps [1000]: "
    )

    if n_steps_input == "":
        n_steps = 1000
    else:
        n_steps = int(n_steps_input)

    step_std_input = input(
        "Step standard deviation [1.0]: "
    )

    if step_std_input == "":
        step_std = 1.0
    else:
        step_std = float(step_std_input)

    x, y = brownian_motion(
        n_steps=n_steps,
        step_std=step_std,
    )

    final_displacement = (
        x[-1] ** 2 + y[-1] ** 2
    ) ** 0.5

    print(
        f"\nFinal displacement: "
        f"{final_displacement:.2f}"
    )

    plot_brownian_motion(
        x=x,
        y=y,
        output_path=str(
            RESULT_FOLDER / "brownian_motion.png"
        ),
    )

    print(
        "Plot saved to "
        "results/monte_carlo/brownian_motion.png"
    )
def run_radioactive_decay():
    n_atoms = int(
        input("Initial number of atoms: ")
    )

    decay_probability = float(
        input("Decay probability per step: ")
    )

    n_steps = int(
        input("Number of time steps: ")
    )

    atoms_remaining = radioactive_decay(
        n_atoms=n_atoms,
        decay_probability=decay_probability,
        n_steps=n_steps,
    )

    print(
        f"\nAtoms remaining after "
        f"{n_steps} steps: "
        f"{atoms_remaining[-1]}"
    )

    plot_radioactive_decay(
        atoms_remaining=atoms_remaining,
        output_path=str(
            RESULT_FOLDER / "radioactive_decay.png"
        ),
    )

    print(
        "Plot saved to "
        "results/monte_carlo/"
        "radioactive_decay.png"
    )