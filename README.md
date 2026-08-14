# Scientific Computing Toolkit

A modular Python toolkit for scientific data analysis, numerical model fitting and Monte Carlo simulation.

The project combines signal processing, mathematical model fitting and stochastic simulation within a common workflow. It was developed as a portfolio project to demonstrate practical software engineering and scientific computing using Python.

---

## Features

### Signal Analysis

- Load experimental signals from CSV files
- Fast Fourier Transform (FFT)
- Dominant frequency detection
- Spectral peak detection
- Signal statistics
- Digital filtering
- Automated analysis reporting

### Curve Fitting

- Linear models
- Exponential decay
- Gaussian models
- Sinusoidal models
- Nonlinear least-squares fitting
- Parameter uncertainty estimation
- Coefficient of determination (R²)

### Monte Carlo Analysis

- Monte Carlo uncertainty analysis for fitted model parameters
- Distribution analysis of fitted parameters
- Visualization of parameter distributions

### Monte Carlo Demonstrations

- Monte Carlo estimation of π
- 2D random walk
- Brownian motion
- Radioactive decay

---

## Integrated Workflow

One of the main goals of the project is to combine the individual numerical methods into a common scientific analysis workflow.

For signal data, the toolkit can perform

```text
CSV measurement data
        ↓
Signal Analysis
        ↓
FFT / Peak Detection
        ↓
Dominant Frequency
        ↓
Sinusoidal Curve Fitting
        ↓
Monte Carlo Uncertainty Analysis
        ↓
Parameter Distributions
```

The dominant frequency determined from the FFT is used as an initial estimate for the sinusoidal fit.

Monte Carlo simulations can then be used to investigate the uncertainty of the fitted model parameters.

---

## Project Structure

```text
scientific-computing-toolkit/
├── data/
│   ├── signal_analysis/
│   └── curve_fitting/
│
├── results/
│   ├── signal_analysis/
│   ├── curve_fitting/
│   └── monte_carlo/
│
├── src/
│   └── scientific_toolkit/
│       ├── data.py
│       │
│       ├── signal_analysis/
│       │   ├── cli.py
│       │   ├── data_loader.py
│       │   ├── filters.py
│       │   ├── metrics.py
│       │   ├── reporting.py
│       │   └── spectrum.py
│       │
│       ├── curve_fitting/
│       │   ├── cli.py
│       │   ├── data_loader.py
│       │   ├── fitting.py
│       │   ├── models.py
│       │   └── plotting.py
│       │
│       └── monte_carlo/
│           ├── cli.py
│           ├── simulations.py
│           ├── plotting.py
│           └── uncertainty.py
│
├── tests/
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository and install the package in editable mode:

```bash
python -m pip install -e .
```

For development and testing:

```bash
python -m pip install -e ".[dev]"
```

---

## Usage

Start the toolkit with

```bash
python main.py
```

The main menu provides access to the different modules:

```text
Scientific Computing Toolkit

1. Signal Analysis
2. Curve Fitting
3. Monte Carlo Demonstrations
4. Exit
```

---

## Input Data

### Signal Analysis

Signal CSV files should contain

```csv
time,signal
```

and should be placed inside

```text
data/signal_analysis/
```

### Curve Fitting

Curve fitting datasets should contain

```csv
x,y
```

and should be placed inside

```text
data/curve_fitting/
```

---

## Example Integrated Analysis

A signal can first be analyzed in the frequency domain.

Example:

```text
Dominant frequency: 50.00 Hz

Detected peaks:
50.00 Hz
150.00 Hz
```

The detected dominant frequency can then be used as the initial estimate for a sinusoidal fit.

Example:

```text
Sine Fit Results

Amplitude: 2.01 ± 0.03
Frequency: 49.99 ± 0.02 Hz
Phase: 0.41 ± 0.02
Offset: 0.20 ± 0.01

R²: 0.995
```

A Monte Carlo uncertainty analysis can subsequently estimate the distribution of the fitted parameters.

---

## Running the Tests

Run all tests with

```bash
python -m pytest
```

---

## Technologies

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Pytest
- Git

---

## Motivation

This project was developed to combine several methods commonly used in experimental physics and scientific computing within a structured software project.

The toolkit demonstrates practical experience with

- signal processing
- numerical optimization
- mathematical modeling
- uncertainty analysis
- stochastic simulation
- automated testing
- modular Python software development

The focus is not only on implementing individual numerical methods, but on integrating them into a reusable scientific analysis workflow.