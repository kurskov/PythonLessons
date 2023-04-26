x = 0

while (n := float(input())) != 0:
    if n >= 500:
        x = x + n * 0.9
    else:
        x = x + n

print(x)
