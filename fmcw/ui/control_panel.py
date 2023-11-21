import typing

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QWidget

from fmcw.controller import RadarController

from .setting_dialog import SettingDialog


class ControlPanel(QGroupBox):
    start_radar = pyqtSignal(str)
    stop_radar = pyqtSignal()

    save_data = pyqtSignal()
    open_setting = pyqtSignal()

    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)

        self.setTitle("Control Panel")

        self.new_layout = QVBoxLayout()
        self.setting_dialog = SettingDialog(self)

        self.buttons = {
            "start": QPushButton("Mulai Radar"),
            "stop": QPushButton("Stop Radar"),
            "save": QPushButton("Save Data"),
            "setting": QPushButton("Setting"),
        }

        for _, button in self.buttons.items():
            self.new_layout.addWidget(button)

        self.buttons["setting"].clicked.connect(self._open_setting_dialog)
        self.buttons["start"].clicked.connect(self._start_radar)
        self.buttons["stop"].clicked.connect(self._stop_radar)
        self.buttons["save"].clicked.connect(self.save_data.emit)

        self.buttons["stop"].setEnabled(False)

        self.new_layout.addStretch()
        self.setLayout(self.new_layout)

    def _open_setting_dialog(self):
        self.setting_dialog.exec()

    def _start_radar(self):
        port: str = self.setting_dialog.get_radar_port()
        self.start_radar.emit(port)

        self.buttons["start"].setEnabled(False)
        self.buttons["stop"].setEnabled(True)

    def _stop_radar(self):
        self.stop_radar.emit()
        self.buttons["start"].setEnabled(True)
        self.buttons["stop"].setEnabled(False)

