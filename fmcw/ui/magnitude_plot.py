import typing

import numpy as np

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QWidget

from fmcw.contrib import PlotCanvasWidget


class MagnitudePlot(QGroupBox):
    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.setTitle("Magnitude Plot")

        self._magnitude_plot = PlotCanvasWidget()
        self._new_layout = QVBoxLayout()

        self._new_layout.addWidget(self._magnitude_plot)

        self.setLayout(self._new_layout)


    def set_plot(self, mag_data: np.ndarray):
        self._magnitude_plot.axes.clear()

        line1 = self._magnitude_plot
        if np.min(mag_data) <= line1.axes.get_ylim()[0] or np.max(mag_data) >= line1.axes.get_ylim()[1]: # type: ignore
            self._magnitude_plot.axes.set_ylim([np.min(mag_data) - np.std(mag_data), np.max(mag_data) + np.std(mag_data)]) # type: ignore

        self._magnitude_plot.axes.plot(mag_data)
        self._magnitude_plot.draw_idle()
