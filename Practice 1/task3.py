# Задание 3: Расчет погрешности

import numpy as np

from task2 import SERIA_1, SERIA_2


def calculate_error(approx_pi):
    # Теоретическое значение числа π
    pi_true = np.pi
    return abs(approx_pi - pi_true) / pi_true * 100


# Погрешности для каждой серии
errors_1 = [calculate_error(pi) for pi in SERIA_1]
errors_2 = [calculate_error(pi) for pi in SERIA_2]

# Усреднение результатов по 5ти сериям
SERIA_MEAN = np.mean([SERIA_1, SERIA_2], axis=0)

# Погрешности для усредненных значений
errors_mean = [calculate_error(pi) for pi in SERIA_MEAN]

print("Средние значения SERIA:", SERIA_MEAN)
print("Погрешности:", errors_mean)
