import logging
import time
import ast
import typing

import serial
import numpy as np

from PyQt5.QtCore import QObject, pyqtSignal


class FMCWRadar(QObject):
    phase_signal_out = pyqtSignal(np.ndarray)
    phase_raw_signal_out = pyqtSignal(list)
    phase_plot_signal_out = pyqtSignal(np.ndarray, np.ndarray)

    magnitude_signal_out = pyqtSignal(np.ndarray)

    reset_buffer = pyqtSignal()
    finished = pyqtSignal()
    err_msg = pyqtSignal(list)

    def __init__(self, fmcw_port: typing.Optional[str] = None) -> None:
        super().__init__()

        self.is_started: bool = False

        self.FMCW_RADAR = serial.Serial(
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )

        if fmcw_port:
            self.FMCW_RADAR.port = fmcw_port

    def set_port(self, port: str):
        self.FMCW_RADAR.port = port

    def stop_radar(self):
        """
        stopping radar from running
        """
        self.get_data = False

        try:
            self.FMCW_RADAR.close()
            self.finished.emit()
        except Exception as e:
            logging.log(10, f"Cannot close peripheral: {e}")

    def _raise_error(self, err_title: str, err_msg: str):
        """
        Quit from the thread.
        """

        try:
            self.FMCW_RADAR.close()
        except Exception:
            pass

        self.err_msg.emit([err_title, err_msg])
        self.finished.emit()

    def _process_data_respiro(self, y_vec, yo_vec):
        return yo_vec[-1] * 0.0048 + yo_vec[-2] * 0.0195 + yo_vec[-3] * 0.0289 + yo_vec[-4] * 0.0193 + yo_vec[-5] * 0.0048 - y_vec[-1] - y_vec[-2] * -2.3695 - y_vec[-3] * 2.3140 - y_vec[-4] * -1.0547 - y_vec[-5] * 0.1874

    def _max_index_value(self, ls) -> tuple:
        """
        return maximum value and it's index from a list
        """

        maxval = max(ls)

        try:
            idx = ls.index(maxval)
        except AttributeError:
            idx = np.where(ls == maxval)[0][0]

        return maxval, idx

    def run(self) -> None:
        if not self.FMCW_RADAR:
            self.err_msg.emit(["Radar Error", "Tidak bisa menjalankan radar karena radar tidak tersambung, hubungi Lukman atau cek koneksi (kabel). 🔌"])
            self.finished.emit()
            return

        try:
            if not self.FMCW_RADAR.is_open:
                logging.info("[INFO] Open the FMCW Radar...")
                self.FMCW_RADAR.open()
        except AttributeError as e:
            self.err_msg.emit(["ERROR: Tidak bisa menggunakan radar", f"Tidak bisa menggunakan radar karena: {e}"])
            self.finished.emit()
            return

        # Reset the buffer from the main gui
        self.reset_buffer.emit(True)

        # Do some clean up, just to make sure
        self.FMCW_RADAR.flush()

        self.FMCW_RADAR.write(str.encode("oF"))
        time.sleep(0.5)
        self.FMCW_RADAR.write(str.encode("oP"))

        y_vec = np.linspace(0, 0, 512)[:-1]
        yo_vec = np.linspace(0, 0, 512)[:-1]
        x_vec = np.linspace(-512, 0, 512)[:-1]

        self.get_data = True
        peak_index = -1

        while self.get_data:
            try:
                radar_data = ast.literal_eval(self.FMCW_RADAR.readline().decode("utf-8"))
            except (SyntaxError, UnicodeDecodeError):
                continue

            if not isinstance(radar_data, dict):
                continue

            phase_data = radar_data.get("Phase")
            magnitude_data = radar_data.get("FFT")

            if phase_data == "Phase" and peak_index > 0:
                yo_vec[-1] = float(phase_data[peak_index]) * 57.29

                self.phase_raw_signal_out.emit(float(yo_vec[-1]))

                y_vec[-1] = self._process_data_respiro(y_vec, yo_vec)
                x_vec += 1

                # phase data after filtering
                self.phase_signal_out.emit(y_vec[-1])

                # phase data after filtering for plotting perpose
                self.phase_plot_signal_out.emit((x_vec) * 0.26, y_vec)

                y_vec = np.append(y_vec[1:], 0.0)
                yo_vec = np.append(yo_vec[1:], 0.0)

            elif magnitude_data:
                self.magnitude_signal_out.emit(magnitude_data[:512])
                _, peak_index = self._max_index_value(magnitude_data[:512])

        try:
            self.FMCW_RADAR.close()
        except AttributeError:
            pass

        self.finished.emit()
