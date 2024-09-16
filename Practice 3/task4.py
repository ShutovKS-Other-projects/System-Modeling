# Задание 4: Построение гистограмм относительных частот
from matplotlib import pyplot as plt

from task3 import N_values, samples

# Построение гистограмм относительных частот для каждого N
plt.figure(figsize=(10, 6))
for i, N in enumerate(N_values):
    plt.subplot(2, 2, i + 1)
    plt.hist(samples[i], bins=100, density=True, alpha=0.6, color='b')
    plt.title(f'Гистограмма для N = {N}')
    plt.xlabel('Значения')
    plt.ylabel('Относительная частота')

plt.tight_layout()
plt.show()
