from math import asin, cos, pi, sqrt

x = float(input())
y = float(input())

a = asin(cos(x + sqrt(3) / 2 * pi))
b = 1.2 * sqrt(2 - cos(y)**2)
c = x**2 + y**2 + 1
z = (a + b) / c

print(round(z, 5))
