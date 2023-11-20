import typing

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QWidget

from .setting_dialog import SettingDialog


class ControlPanel(QGroupBox):
    toggle_radar = pyqtSignal(bool)
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

        self.new_layout.addStretch()
        self.setLayout(self.new_layout)

    def _open_setting_dialog(self):
        self.setting_dialog.exec()

