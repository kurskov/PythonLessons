n = int(input())

n0 = n % 10
n1 = n // 10 % 10
n2 = n // 100 % 10

if n2 >= n1:
    if n1 >= n0:
        print(f"{n2}{n1} {n1}{n0}")
