"""Упражнение №10: «цветок»

Нарисуйте «цветок» из окружностей.
Используйте функцию, рисующую окружность.
"""

import turtle


def draw_circle(direction):
    for i in range(180):
        turtle.forward(1)
        if direction == "cw":
            turtle.right(2)
        elif direction == "ccw":
            turtle.left(2)


for i in range(3):
    draw_circle("ccw")
    draw_circle("cw")
    turtle.left(60)
