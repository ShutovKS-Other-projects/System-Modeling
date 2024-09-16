# Задание №7

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chisquare

from task2 import N, A, B
from task5 import left, right, num_intervals, relative_frequencies
from task6 import expected_frequencies

# Генерация последовательности с использованием встроенного генератора
sequence_builtin = np.random.uniform(A, B, N)

# Рассчитаем математическое ожидание и дисперсию для встроенного генератора
mean_builtin = np.mean(sequence_builtin)
variance_builtin = np.var(sequence_builtin)

# Определение относительных частот для встроенного генератора
rel_freqs_builtin = relative_frequencies(sequence_builtin, left, right, num_intervals)

# Построим гистограмму для встроенного генератора
plt.hist(sequence_builtin, bins=num_intervals, density=True, edgecolor='black')
plt.title("Гистограмма относительных частот (встроенный генератор)")
plt.show()

# Рассчитаем критерий Пирсона для встроенного генератора
observed_frequencies_builtin = np.histogram(sequence_builtin, bins=num_intervals, range=(left, right))[0]
chi2_builtin, p_value_builtin = chisquare(observed_frequencies_builtin, expected_frequencies)
