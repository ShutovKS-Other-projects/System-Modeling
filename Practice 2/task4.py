# Задание №4

from task2 import sequence


def find_period(sequence):
    seen = {}
    for i, num in enumerate(sequence):
        if num in seen:
            return i - seen[num]
        seen[num] = i
    return None


# Определение периода
period = find_period(sequence)
