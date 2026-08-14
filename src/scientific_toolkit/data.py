from dataclasses import dataclass
import numpy as np


@dataclass
class MeasurementData:
    x: np.ndarray
    y: np.ndarray
    name: str = ""