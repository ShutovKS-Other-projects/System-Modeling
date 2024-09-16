# Задание 3: Моделирование нормального распределения методом обратной функции
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


# Метод обратной функции для моделирования нормального распределения
def inverse_transform_method(N, M=10, sigma=2):
    u = np.random.rand(N)
    return norm.ppf(u, loc=M, scale=sigma)


# Моделирование для разных N
N_values = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
samples = [inverse_transform_method(N) for N in N_values]

# Построение гистограмм для каждого N
plt.figure(figsize=(10, 6))
for i, N in enumerate(N_values):
    plt.subplot(2, 2, i + 1)
    plt.hist(samples[i], bins=100, density=True, alpha=0.6, color='g')
    plt.title(f'N = {N}')
    plt.xlabel('Значения')
    plt.ylabel('Частота')

plt.tight_layout()
plt.show()
