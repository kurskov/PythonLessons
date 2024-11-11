from math import radians, e, sin, cos, log
import matplotlib.pyplot as plt


def f_x(x):

    x = radians(x)
    y = e ** cos(x) + log(sin(0.8 * x) ** 2 + 1) * cos(x)

    return y


def y_x(x):

    x = radians(x)
    y = -log((sin(x) + cos(x)) ** 2 + 1.7) + 2

    return y


a, b = -240, 360
n = b - a + 1
h = (b - a) / (n - 1)
x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]

line_f = plt.plot(x_list, f_list, label='f(x)', color="blue", linewidth=2)
line_y = plt.plot(x_list, y_list, label='y(x)', color="red", linewidth=2)

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.legend()
plt.title("Графики функций")

plt.show()
