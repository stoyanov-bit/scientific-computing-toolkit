

def run_curve_fitting():
    
    import numpy as np
    from pathlib import Path
        

    from scientific_toolkit.curve_fitting.data_loader import load_xy_csv
    from scientific_toolkit.curve_fitting.fitting import fit_model, compute_r_squared
    from scientific_toolkit.curve_fitting.plotting import plot_fit
    from scientific_toolkit.curve_fitting.models import linear, exponential_decay, gaussian, sine


    MODELS = {
        "1": {
            "name": "Linear",
            "function": linear,
            "initial_guess": [1.0, 0.0],
            "parameters": ["a", "b"],
        },
        "2": {
            "name": "Exponential decay",
            "function": exponential_decay,
            "initial_guess": [1.0, 0.5, 0.0],
            "parameters": ["amplitude", "decay_rate", "offset"],
        },
        "3": {
            "name": "Gaussian",
            "function": gaussian,
            "initial_guess": [1.0, 5.0, 1.0, 0.0],
            "parameters": ["amplitude", "center", "sigma", "offset"],
        },
        "4": {
            "name": "Sine",
            "function": sine,
            "initial_guess": [2.0, 0.6, 0.4, 0.2],
            "parameters": ["amplitude", "frequency", "phase", "offset"],
        },
    }


    data_folder = Path("data/curve_fitting")
    result_folder = Path("results/curve_fitting")
    result_folder.mkdir(exist_ok=True)

    csv_files = list(data_folder.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data folder.")
        return

    print("Available CSV files:")
    for index, file in enumerate(csv_files, start=1):
        print(f"{index}. {file.name}")

    file_choice = int(input("\nChoose file number: "))
    csv_path = csv_files[file_choice - 1]

    print("\nAvailable models:")
    for key, model_info in MODELS.items():
        print(f"{key}. {model_info['name']}")

    model_choice = input("\nChoose model number: ")
    model_info = MODELS[model_choice]
    
    data = load_xy_csv(str(csv_path))
    x = data.x
    y= data.y


    parameters, covariance = fit_model(
        model=model_info["function"],
        x=x,
        y=y,
        initial_guess=model_info["initial_guess"],
    )

    parameter_errors = np.sqrt(np.diag(covariance))

    y_fit = model_info["function"](x, *parameters)
    r_squared = compute_r_squared(y, y_fit)

    print(f"\nLoaded file: {csv_path.name}")
    print(f"Selected model: {model_info['name']}")
    print(f"R²: {r_squared:.4f}")

    print("\nFit parameters:")
    for name, value, error in zip(
        model_info["parameters"],
        parameters,
        parameter_errors,
    ):
        print(f"{name}: {value:.4f} ± {error:.4f}")

    output_plot = result_folder / f"{csv_path.stem}_{model_info['name'].lower().replace(' ', '_')}.png"
    plot_fit(
        x=x,
        y=y,
        y_fit=y_fit,
        output_path=str(output_plot),
        model_name=model_info["name"],
        parameter_names=model_info["parameters"],
        parameters=parameters,
        parameter_errors=parameter_errors,
        r_squared=r_squared,
    )

    print(f"\nPlot saved to: {output_plot}")