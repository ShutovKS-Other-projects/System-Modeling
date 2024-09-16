# Задание 5: Средняя квадратичная погрешность
import numpy as np
from matplotlib import pyplot as plt

from task1 import normal_distribution
from task3 import samples, N_values


# Функция для вычисления средней квадратичной погрешности
def mse_theoretical_vs_experimental(sample, M=10, sigma=2, bins=100):
    hist, bin_edges = np.histogram(sample, bins=bins, density=True)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2
    theoretical_pdf = normal_distribution(bin_centers, M, sigma)
    mse = np.mean((hist - theoretical_pdf) ** 2)
    return mse


# Расчет средней квадратичной погрешности для каждого N
mse_values = [mse_theoretical_vs_experimental(samples[i], M=10, sigma=2) for i in range(len(N_values))]

# Построение графика зависимости MSE от числа экспериментов
plt.figure(figsize=(8, 5))
plt.plot(N_values, mse_values, marker='o', linestyle='-', color='r')
plt.xscale('log')
plt.title('Средняя квадратичная погрешность от числа экспериментов')
plt.xlabel('Число экспериментов (N)')
plt.ylabel('Средняя квадратичная погрешность (MSE)')
plt.grid(True)
plt.show()
