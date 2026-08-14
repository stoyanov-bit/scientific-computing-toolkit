import pandas as pd

from scientific_toolkit.data import MeasurementData


def load_signal_csv(filepath: str) -> MeasurementData:
    df = pd.read_csv(filepath)

    return MeasurementData(
        x=df["time"].to_numpy(),
        y=df["signal"].to_numpy(),
        name=filepath,
    )