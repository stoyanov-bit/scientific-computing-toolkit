from scientific_toolkit.signal_analysis.cli import (
    run_signal_analysis,
)

from scientific_toolkit.curve_fitting.cli import (
    run_curve_fitting,
)

from scientific_toolkit.monte_carlo.cli import (
    run_monte_carlo,
)


def main():

    while True:

        print(
            "\nScientific Computing Toolkit"
        )

        print(
            "1. Signal Analysis"
        )

        print(
            "2. Curve Fitting"
        )

        print(
            "3. Monte Carlo Demonstrations"
        )

        print(
            "4. Exit"
        )

        choice = input(
            "\nChoose option: "
        )

        if choice == "1":
            run_signal_analysis()

        elif choice == "2":
            run_curve_fitting()

        elif choice == "3":
            run_monte_carlo()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    main()