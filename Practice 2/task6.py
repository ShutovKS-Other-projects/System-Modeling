# Задание №6

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare

from task2 import N, sequence_scaled
from task5 import left, right, num_intervals

# Построение гистограммы
plt.hist(sequence_scaled, bins=num_intervals, density=True, edgecolor='black')
plt.title("Гистограмма относительных частот")
plt.show()

# Расчет критерия Пирсона
observed_frequencies = np.histogram(sequence_scaled, bins=num_intervals, range=(left, right))[0]
expected_frequencies = [N / num_intervals] * num_intervals
chi2, p_value = chisquare(observed_frequencies, expected_frequencies)
