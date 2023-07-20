"""Упражнение №7: спираль

Нарисуйте спираль.
"""

import turtle

turtle.shape('turtle')
for i in range(3600):
    turtle.forward(i/50)
    turtle.left(4)
