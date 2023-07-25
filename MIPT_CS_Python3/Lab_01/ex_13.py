"""Упражнение №13: смайлик

Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.
"""

import turtle


def draw_circle(direction, radius, fill="white"):
    turtle.fillcolor(fill)
    turtle.begin_fill()
    for i in range(90):
        turtle.forward(radius)
        if direction == "cw":
            turtle.right(4)
        elif direction == "ccw":
            turtle.left(4)
    turtle.end_fill()


def draw_arc(radius):
    for i in range(45):
        turtle.forward(radius)
        turtle.right(4)


def jump(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


draw_circle("ccw", 5, "yellow")

jump(-20, 80)
draw_circle("ccw", 0.5, "blue")
jump(20, 80)
draw_circle("ccw", 0.5, "blue")

jump(0, 80)
turtle.right(90)
turtle.width(6)
turtle.forward(20)

jump(40, 50)
turtle.color("red")
draw_arc(2.5)
