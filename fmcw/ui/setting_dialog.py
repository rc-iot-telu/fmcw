import typing
import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog, QFormLayout, QLineEdit,
    QPushButton, QTextEdit, QWidget
)

from fmcw.contrib import get_asset, AssetType, get_popup, PopUpLevel

from serial.tools.list_ports import comports



class SettingDialog(QDialog):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Setting Radar Application")
        self.setMinimumSize(280, 320)

        self.new_layout = QFormLayout()
        self.new_layout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.new_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.new_layout.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.new_layout.setLabelAlignment(Qt.AlignLeft)

        refresh_btn = QPushButton("Refresh Port")
        save_btn = QPushButton("Save Setting")

        self.radar_port = QLineEdit()
        self.port_avail = QTextEdit()

        self.new_layout.addRow("FMCW Port", self.radar_port)
        self.new_layout.addRow("Detected Port", self.port_avail)
        self.new_layout.addRow(save_btn)
        self.new_layout.addRow(refresh_btn)

        save_btn.clicked.connect(self._save_data)
        refresh_btn.clicked.connect(self._refresh_port)

        self._load_data()
        self._refresh_port()
        self.setLayout(self.new_layout)

    def _save_data(self):
        data = {}
        path = get_asset("setting.dat", AssetType.OBJECT)

        data["PORT_RADAR"] = self.radar_port.text()

        with open(path, "wb") as obj:
            pickle.dump(data, obj)

        get_popup("Successfully Save Configuration!", PopUpLevel.INFO, self)

    def _load_data(self):
        data = {}
        path = get_asset("setting.dat", AssetType.OBJECT)

        try:
            fileObj = open(path, "rb")
        except FileNotFoundError:
            return

        try:
            data.update(pickle.load(fileObj))
        except EOFError:
            return

        fileObj.close()

        self.radar_port.setText(data.get("PORT_RADAR"))

    def _refresh_port(self):
        ports = comports()

        if len(ports) < 1:
            self.port_avail.setText("Tidak ada perangkat yang terhubung!")
            return

        ports = ["{}: {} [{}]\n".format(port, desc, hwid) for port, desc, hwid in sorted(ports)]
        self.port_avail.setText("".join(ports))
