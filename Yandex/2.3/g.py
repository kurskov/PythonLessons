a = a1 = int(input())
b = b1 = int(input())

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(int(a1 * b1 / a))
