"""Упражнение №4: окружность

Нарисуйте окружность. Воспользуйтесь тем фактом,
что правильный многоугольник с большим числом сторон будет выглядеть
как окружность.
"""

import turtle

turtle.shape('turtle')
for i in range(90):
    turtle.forward(5)
    turtle.left(4)