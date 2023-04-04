import pywt
import numpy as np
import matplotlib.pyplot as plt

# Загрузка сигнала EMG
# file_path = filedialog.askopenfilename(filetypes=[("Asc file", "*.asc")])
data = np.loadtxt("data/срезз.asc", skiprows=4)
# emg_signal = data
emg_signal = data[:, 1]

# Определение типа вейвлет-функции и уровня декомпозиции
wavelet = 'db6'
level = 1

# Декомпозиция сигнала с помощью вейвлет-функции
coefficients = pywt.wavedec(emg_signal, wavelet, level=level)

# Удаление высокочастотных коэффициентов
coefficients[1:] = map(lambda x: np.zeros_like(x), coefficients[1:])

# Восстановление сигнала из коэффициентов
filtered_emg_signal = pywt.waverec(coefficients, wavelet)

# Рисуем графики
plt.figure(figsize=(12,6))
plt.subplot(311)
plt.plot(emg_signal)
plt.title('Исходный сигнал')

plt.subplot(312)
plt.plot(filtered_emg_signal)
plt.title('Отфильтрованный сигнал')

plt.subplot(313)
plt.plot(emg_signal, label='Исходный сигнал')
plt.plot(filtered_emg_signal, label='Отфильтрованный сигнал')
plt.legend()
plt.title('Сравнение исходного и отфильтрованного сигналов')

plt.tight_layout()
plt.show()
# # Отображение исходного сигнала
# plt.subplot(2, 1, 1)
# plt.plot(emg_signal)
# plt.xlabel('Время') # подписываем ось X
# plt.ylabel('Амплитуда') # подписываем ось Y
# plt.title('Original EMG Signal')
#
# # Отображение отфильтрованного сигнала
# plt.subplot(2, 1, 2)
# plt.plot(filtered_emg_signal)
# plt.xlabel('Время') # подписываем ось X
# plt.ylabel('Амплитуда') # подписываем ось Y
# plt.title('Filtered EMG Signal')
#
# plt.tight_layout()
# plt.show()