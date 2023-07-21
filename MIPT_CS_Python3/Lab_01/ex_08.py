"""Упражнение №8: квадратная «спираль»

Нарисуйте «квадратную» спираль.
"""

import turtle

turtle.shape('turtle')
for i in range(20):
    turtle.forward(10 + i * 5)
    turtle.left(90)
