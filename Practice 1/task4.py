# Задание 4: Вычисление определенного интеграла

import random

import numpy as np


def f(x):
    return 3 + x


def monte_carlo_integral(a, b, ExpNmb):
    total = 0

    for _ in range(ExpNmb):
        x = random.uniform(a, b)
        total += f(x)

    integral = (b - a) * total / ExpNmb
    return integral


# Считаем интеграл для разных значений экспериментов
experiments_integral = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
integral_results = [monte_carlo_integral(0, 2, ExpNmb) for ExpNmb in experiments_integral]

# Вычисление усредненного значения и погрешности
integral_mean = np.mean(integral_results)
true_integral = 7  # Точное значение интеграла для f(x) на [0, 2]
integral_error = abs(integral_mean - true_integral) / true_integral * 100

print("Результаты интеграла:", integral_results)
print("Среднее значение интеграла:", integral_mean)
print("Погрешность интеграла:", integral_error)
