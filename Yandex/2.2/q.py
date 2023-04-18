a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif (a == 0 and b == 0 and c != 0) or d < 0:
    print("No solution")
elif a == 0:
    x = -c / b
    print(f"{x:.2f}")
elif d == 0:
    x = -b / (2 * a)
    print(f"{x:.2f}")
else:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    x = sorted({x1, x2})
    print(f"{x[0]:.2f} {x[1]:.2f}")
