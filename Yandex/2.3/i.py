n = int(input())

if n > 0:
    for i in range(n - 1, 0, -1):
        n *= i
    print(int(n))
else:
    print(1)
