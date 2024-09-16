# Задание №5

from task2 import sequence_scaled


def relative_frequencies(sequence, left, right, num_intervals):
    interval_width = (right - left) / num_intervals
    intervals = [0] * num_intervals

    for num in sequence:
        if left <= num < right:
            idx = int((num - left) / interval_width)
            intervals[idx] += 1

    total = len(sequence)
    relative_freqs = [count / total for count in intervals]
    return relative_freqs


# Пример вызова функции
left, right, num_intervals = 0, 10, 10
rel_freqs = relative_frequencies(sequence_scaled, left, right, num_intervals)
