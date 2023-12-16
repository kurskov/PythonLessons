from math import sqrt


def compute_len(x_0, y_0, x_1, y_1):

    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)

    return len_line


def compute_area(a_1, a_2, a_3):

    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))

    return area


def compute_med(a, b ,c):

    med = sqrt(2 * (b**2 + c**2)- a**2) / 2

    return med


x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a + c <= b:

    print("error")

else:

    p = a + b + c
    s = compute_area(a, b, c)

    r_in = 2 * s / p
    r_out = (a * b * c) / (4 * s)
    sum_med = compute_med(a, b, c) + compute_med(b, c, a) + compute_med(c, a, b)

    print(round(r_in, 4), round(r_out, 4), round(sum_med, 4))
