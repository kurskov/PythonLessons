"""Упражнение №11: «бабочка»

Нарисуйте «бабочку» из окружностей.
Используйте функцию, рисующую окружность.
"""

import turtle


def draw_circle(direction, radius):
    for i in range(90):
        turtle.forward(radius)
        if direction == "cw":
            turtle.right(4)
        elif direction == "ccw":
            turtle.left(4)


turtle.left(90)
for i in range(1, 5):
    draw_circle("ccw", i + 5)
    draw_circle("cw", i + 5)
