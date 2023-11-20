import sys
import os
import qdarktheme

from PyQt5.QtWidgets import QApplication

from fmcw import MainWindows




def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication([])

    ex = MainWindows()
    ex.setMinimumSize(1280, 720)
    ex.show()


    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
