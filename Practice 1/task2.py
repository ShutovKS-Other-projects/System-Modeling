# Задание 2: Расчеты с разным количеством экспериментов

import task1


def run_series(x0, y0, r0, experiments):
    results = []

    for ExpNmb in experiments:
        pi_value = task1.calc_pi(x0, y0, r0, ExpNmb)
        results.append(pi_value)

    return results


# Число экспериментов для каждой серии
experiments_1 = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
experiments_2 = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]

# Выполнение расчета для всех серий
SERIA_1 = run_series(10, 20, 50, experiments_1)
SERIA_2 = run_series(10, 20, 50, experiments_2)
