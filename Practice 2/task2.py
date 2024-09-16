# Задание №2

from task1 import multiplicative_rng

# Параметры
a = 22695477
b = 1
m = 2 ** 32
X0 = 1
N = 10 ** 6

# Генерация последовательности
sequence = multiplicative_rng(a, b, m, X0, N)

# Преобразование в интервал [A, B]
A = 0
B = 10
sequence_scaled = [A + (B - A) * x for x in sequence]
