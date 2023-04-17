n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

a = (k1 - m) / (m - k2)

n2 = int(n * a / (1 + a))
n1 = int(n - n2)

print(f"{n1} {n2}")
