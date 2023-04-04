import pywt
import numpy as np


# Загрузка сигнала EMG
def filtering_data(data):
    emg_signal = data
    # Определение типа вейвлет-функции и уровня декомпозиции
    wavelet = 'db4'
    level = 1
    # Декомпозиция сигнала с помощью вейвлет-функции
    coefficients = pywt.wavedec(emg_signal, wavelet, level=level)
    # Удаление высокочастотных коэффициентов
    coefficients[1:] = map(lambda x: np.zeros_like(x), coefficients[1:])
    # Восстановление сигнала из коэффициентов
    filtered_emg_signal = pywt.waverec(coefficients, wavelet)
    return filtered_emg_signal


def read_data(file_path):
    data = np.loadtxt(file_path, skiprows=4)
    if isinstance(data[0], (list, tuple, np.ndarray)):
        return data[:, 1]
    return data
