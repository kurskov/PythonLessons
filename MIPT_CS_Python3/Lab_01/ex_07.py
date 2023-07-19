"""Упражнение №7: спираль

Нарисуйте спираль.
"""

import turtle

turtle.shape('turtle')
for i in range(3600):
    turtle.forward(4 + i)
    turtle.left(4 + i)
