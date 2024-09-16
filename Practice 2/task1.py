# Задание №1

def multiplicative_rng(a, b, m, X0, N):
    sequence = []
    X = X0
    for _ in range(N):
        X = (a * X + b) % m
        sequence.append(X / m)  # нормализуем результат в интервале [0, 1]
    return sequence
