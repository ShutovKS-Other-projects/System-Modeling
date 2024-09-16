# Задание 1: Плотность вероятности нормального распределения

import numpy as np
import matplotlib.pyplot as plt


# Функция плотности вероятности нормального распределения
def normal_distribution(x, M, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - M) ** 2) / (2 * sigma ** 2))


# Параметры
x = np.linspace(-10, 30, 1000)

# Параметры для графиков
params = [
    (10, 2),  # M = 10, σ = 2
    (10, 1),  # M = 10, σ = 1
    (12, 1),  # M = 12, σ = 1
    (15, 2),  # M = 15, σ = 2
]

# Построение графиков
plt.figure(figsize=(10, 6))
for M, sigma in params:
    plt.plot(x, normal_distribution(x, M, sigma), label=f'M={M}, σ={sigma}')

plt.title('Плотность вероятности нормального распределения')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()
