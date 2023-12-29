import math


def f_x(x):

    try:
        y = 1 / (x+1) + x / (x-3)

    except ZeroDivisionError:
        y = math.inf

    return y


s = input("x_list = ")

x_list = [float(x) for x in s.split()]

for x in x_list:
    y = f_x(x)
    print("f(%4.2f) = %6.3f" % (x,  y))
