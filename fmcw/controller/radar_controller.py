import logging
import typing

import numpy as np


from PyQt5.QtCore import QObject, QThread, pyqtSignal

from fmcw.radar import FMCWRadar


class RadarController(QObject):
    def __init__(self, parent: typing.Optional['QObject'] = None) -> None:
        super().__init__(parent)

        self.radar = FMCWRadar()
        self.radar_thread = QThread(self)

    def connect_phase_signal_out(self, func):
        if not callable(func):
            logging.error("argument supplied not eppear to be a function.")
            return

        self.radar.phase_raw_signal_out.connect(func)

    def connect_phase_plot_signal_out(self, func):
        if not callable(func):
            logging.error("argument supplied not eppear to be a function.")
            return

        self.radar.phase_plot_signal_out.connect(func)

    def connect_magnitude_signal_out(self, func):
        if not callable(func):
            logging.error("argument supplied not eppear to be a function.")
            return

        self.radar.magnitude_signal_out.connect(func)

    def start_radar(self, port: str):
        self.radar.set_port(port)
        self.radar.moveToThread(self.radar_thread)

        self.radar_thread.started.connect(self.radar.run)

        self.radar.finished.connect(self.radar_thread.quit)
        self.radar_thread.finished.connect(self.radar.stop_radar)

        self.radar_thread.start()

    def stop_radar(self):
        self.radar.stop_radar()

