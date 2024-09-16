# Задание 1: Реализация подпрограммы CALC_PI

import random


def calc_pi(x0, y0, r0, ExpNmb):
    hits = 0

    for _ in range(ExpNmb):
        # Случайные точки в квадрате [-r0, r0] относительно центра окружности (x0, y0)
        x = random.uniform(x0 - r0, x0 + r0)
        y = random.uniform(y0 - r0, y0 + r0)

        # Проверяем, попала ли точка внутрь окружности
        if (x - x0) ** 2 + (y - y0) ** 2 <= r0 ** 2:
            hits += 1

    # Приближение числа pi
    pi_approx = 4 * hits / ExpNmb
    return pi_approx