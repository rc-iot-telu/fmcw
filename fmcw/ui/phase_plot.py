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

        self._phase_plot = PlotCanvasWidget()
        self.new_layout = QVBoxLayout()

        self.new_layout.addWidget(self._phase_plot)

        self.setLayout(self.new_layout)

    def set_plot(self, x_vec: list, y_vec: list):
        self._phase_plot.axes.clear()

        line1 = self._phase_plot
        if np.min(y_vec) <= line1.axes.get_ylim()[0] or np.max(y_vec) >= line1.axes.get_ylim()[1]: # type: ignore
            self._phase_plot.axes.set_ylim([np.min(y_vec) - np.std(y_vec), np.max(y_vec) + np.std(y_vec)]) # type: ignore

        self._phase_plot.axes.plot(x_vec, y_vec, "-o")
        self._phase_plot.draw_idle()
