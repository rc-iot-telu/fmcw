import typing

import numpy as np

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QWidget

from fmcw.contrib import PlotCanvasWidget


class PhasePlot(QGroupBox):
    set_magnitude_data = pyqtSignal(np.ndarray)
    set_scale = pyqtSignal(tuple)

    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.setTitle("Phase Plot")

        self.magnitude_plot = PlotCanvasWidget()
        self.new_layout = QVBoxLayout()

        self.new_layout.addWidget(self.magnitude_plot)

        self.setLayout(self.new_layout)
