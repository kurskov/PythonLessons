"""Упражнение №6: паук

Нарисуйте паука с n лапами.
"""

import turtle

turtle.shape('turtle')
n = 12
for i in range(n):
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180 + 360 / n)
