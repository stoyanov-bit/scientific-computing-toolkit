from scientific_toolkit.data import MeasurementData
import pandas as pd

def load_xy_csv(filepath: str) -> MeasurementData:
    df = pd.read_csv(filepath)

    return MeasurementData(
        x=df["x"].to_numpy(),
        y=df["y"].to_numpy(),
        name=filepath,
    )