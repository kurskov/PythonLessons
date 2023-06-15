"""Упражнение №3

Постройте график функции
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100.01, 0.01)
y = "np.log((x**2 + 1) * np.exp(-np.abs(x) / 10)) / \
     np.log(1 + np.tan(1 / (1 + np.sin(x)**2)))"
plt.plot(x, eval(y))
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.grid(True)
plt.show()
