import typing

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QGridLayout, QMainWindow,
    QWidget
)

from fmcw.contrib import get_asset, AssetType
from fmcw.controller import RadarController
from fmcw.ui import ControlPanel, MagnitudePlot, PhasePlot


class MainWindows(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("FMCW Radar | PUI-PT Intelligent Sensing IoT")
        self.setWindowIcon(QIcon(get_asset("logo.png", AssetType.IMAGE)))

        # UI Component
        self.control_panel = ControlPanel(self)
        self.magnutide_plot = MagnitudePlot(self)
        self.phase_plot = PhasePlot(self)

        # Layout
        self.new_layout = QGridLayout()

        # Controller
        self.radar_controller = RadarController(self)

        self.new_layout.addWidget(self.control_panel, 0, 0, 2, 1)
        self.new_layout.addWidget(self.magnutide_plot, 0, 1, 1, 1)
        self.new_layout.addWidget(self.phase_plot, 1, 1, 1, 1)

        self.new_layout.setColumnStretch(0, 10)
        self.new_layout.setColumnStretch(1, 77)

        self.new_layout.setRowStretch(0, 50)
        self.new_layout.setRowStretch(1, 50)

        self.widget = QWidget(self)
        self.widget.setLayout(self.new_layout)

        self.control_panel.start_radar.connect(self.radar_controller.start_radar)
        self.control_panel.stop_radar.connect(self.radar_controller.stop_radar)

        self.radar_controller.connect_magnitude_signal_out(
            self.magnutide_plot.set_plot
        )
        self.radar_controller.connect_phase_plot_signal_out(
            self.phase_plot.set_plot
        )

        self.setCentralWidget(self.widget)
