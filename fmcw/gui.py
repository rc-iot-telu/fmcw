import typing

from PyQt5.QtWidgets import QMainWindow, QWidget



class MainWindows(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("FMCW Radar | PUI-PT Intelligent Sensing IoT")


