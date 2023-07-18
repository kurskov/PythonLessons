"""Упражнение №5: больше квадратов

Нарисуйте 10 вложенных квадратов.
"""

import turtle

turtle.shape('turtle')
for j in range(10):
    turtle.penup()
    turtle.goto(-10 * j, -10 * j)
    turtle.pendown()
    for i in range(4):
        turtle.forward(50 + j * 20)
        turtle.left(90)
