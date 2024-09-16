# Задание №3

import numpy as np

from task2 import sequence_scaled
from task2 import A, B

# Рассчитываем математическое ожидание и дисперсию
mean_empirical = np.mean(sequence_scaled)
variance_empirical = np.var(sequence_scaled)

# Теоретические значения для равномерного распределения на [A, B]
mean_theoretical = (A + B) / 2
variance_theoretical = (B - A) ** 2 / 12

(mean_empirical, variance_empirical), (mean_theoretical, variance_theoretical)
