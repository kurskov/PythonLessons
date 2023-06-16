"""Упражнение №2

Постройте график функции

y(x) = x*x - x - 6

и по графику найдите найдите корни уравнения y(x) = 0.
(Не нужно применять численных методов — просто приблизьте график
к корням функции настолько, чтобы было удобно их найти.)
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.5, 4, 0.01)
plt.plot(x, x**2 - x - 6)
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.grid(True)
plt.show()

# -2, 3
