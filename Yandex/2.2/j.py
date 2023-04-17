n = int(input())

n0 = n % 10
n1 = n // 10 % 10
n2 = n // 100 % 10

s1 = n0 + n1
s2 = n1 + n2

if s1 >= s2:
    print(f"{s1}{s2}")
else:
    print(f"{s2}{s1}")
