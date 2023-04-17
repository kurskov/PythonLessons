n = int(input())

n0 = n % 10
n1 = n // 10 % 10
n2 = n // 100 % 10

n_max = max(n0, n1, n2)
n_min = min(n0, n1, n2)

if ((n0 + n1 + n2 - n_max - n_min) * 2) == (n_max + n_min):
    print("YES")
else:
    print("NO")
