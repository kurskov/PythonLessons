"""Упражнение №14: звезды

Нарисуйте две звезды: одну с 5 вершинами, другую — с 11.
Используйте функцию, рисующую звезду с n вершинами.
"""

import turtle


def draw_star(n):
    for _ in range(n):
        turtle.forward(100)
        turtle.right(180 - (180 / n))


draw_star(5)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
draw_star(11)
