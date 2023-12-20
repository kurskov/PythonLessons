from math import ceil

a = float(input())
b = float(input())
v = int(input())

if a <= 0 or b <= 0 or v <= 0:

    print("error")

else:

    paint = 5 * a**2 * b
    cans_number = ceil(paint / (v * 1000))

    print(cans_number)
