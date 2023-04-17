n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

n1 = int(n * (m - k2) / (k1 - k2))
n2 = n - n1

print(f"{n1} {n2}")
