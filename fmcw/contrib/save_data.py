import typing
import os
import csv

from pathlib import Path
from datetime import datetime
from enum import Enum

import numpy as np

class RadarData(Enum):
    MAG = "magnitude"
    PHASA = "phase"


def save_data_to_csv(data: typing.Union[list, np.ndarray], data_kind: RadarData):
    if len(data) < 1:
        return

    path = Path(f"~/Documents/{data_kind.value}")
    today = datetime.strftime(datetime.today(), "%d-%b-%Y %H.%M.%S")

    if not path.expanduser().exists():
        os.makedirs(path.expanduser())

    with open(f"{os.path.join(path.expanduser(), today)}.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for d in data:
            csv_writer.writerows([d])
