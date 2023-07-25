"""Упражнение №12: пружина

Нарисуйте пружину. Используйте функцию, рисующую дугу.
"""

import turtle


def draw_arc(radius):
    for i in range(45):
        turtle.forward(radius)
        turtle.right(4)


turtle.left(90)
for i in range(1, 6):
    draw_arc(3)
    draw_arc(1)
