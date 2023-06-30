"""Упражнение №1

Запишите выражение, заданное формулой, в виде, подходящем для языка Python.
И найдите его значения в точках 1, 10, 1000.
"""

import numpy as np

for x in 1, 10, 1000:
    y = np.log(np.e ** (1 / (np.sin(x) + 1)) / (5 / 4 + 1 / x**15)) / \
     np.log(1 + x**2)
    print(y)
