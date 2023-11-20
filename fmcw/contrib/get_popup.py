from enum import Enum
import typing

from PyQt5.QtWidgets import QMessageBox, QWidget


class PopUpLevel(Enum):
    INFO = 1
    WARN = 2
    CRITICAL = 3


def get_popup(message: str, level: PopUpLevel, parent: typing.Optional[QWidget] = None):

    if level.INFO:
        QMessageBox.information(parent, "Information", message)
    elif level.WARN:
        QMessageBox.warning(parent, "Warning", message)
    else:
        QMessageBox.critical(parent, "Critical", message)
