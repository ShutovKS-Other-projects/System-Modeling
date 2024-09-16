# Задание 2: Функция распределения (CDF) для нормального закона

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

# Параметры
M = 10
sigma = 2
x = np.linspace(0, 20, 1000)

# Функция распределения (CDF)
cdf = norm.cdf(x, loc=M, scale=sigma)

# Построение графика
plt.figure(figsize=(8, 5))
plt.plot(x, cdf, label=f'CDF с M={M}, σ={sigma}')
plt.title('Функция распределения для нормального закона')
plt.xlabel('x')
plt.ylabel('CDF')
plt.grid(True)
plt.legend()
plt.show()
