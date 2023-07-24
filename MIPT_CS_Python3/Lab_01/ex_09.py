"""Упражнение №9: правильные многоугольники

Нарисуйте 10 вложенных правильных многоугольников.
Используйте функцию, рисующую правильный n-угольник.
"""

import turtle
import math


def draw_poligon(n):
    for i in range(n):
        turtle.forward(2 * radius * math.sin(math.pi / n))
        turtle.left(360 / n)


turtle.shape('turtle')
for i in range(3, 13):
    radius = -20 + i * 10
    turtle.penup()
    turtle.goto(radius, 0)
    turtle.pendown()
    turtle.left(360 / (2 * i) + 90)
    draw_poligon(i)
    turtle.right(360 / (2 * i) + 90)
