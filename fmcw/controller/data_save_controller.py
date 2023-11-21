import typing


from PyQt5.QtCore import QObject

from fmcw.contrib import RadarData, get_popup, save_data_to_csv, PopUpLevel


class DataController(QObject):
    def __init__(self, parent: typing.Optional['QObject'] = None) -> None:
        super().__init__(parent)
        self._set_buffer()

    def _set_buffer(self):
        self.data = {
            RadarData.PHASA: [],
            RadarData.MAG: [],
        }

    def save_data(self):
        is_sucess = False

        for label, data in self.data.items():
            is_sucess = save_data_to_csv(data, label)

        if is_sucess:
            get_popup("Successfully save data!", PopUpLevel.INFO)
        else:
            get_popup("Failed save data!", PopUpLevel.CRITICAL)

    # TODO: consolidate two function into one
    def append_data_phase(self, phase_data: list):
        self.data[RadarData.PHASA].append(phase_data)

    def append_data_mag(self, mag_data: list):
        self.data[RadarData.MAG].append(mag_data)

