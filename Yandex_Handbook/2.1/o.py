n = int(input())
m = int(input())
t = int(input())
t0 = n * 60 + m
t1 = t0 + t
h = ((t1 // 60) % 24) + 100
h0 = h % 10
h1 = h // 10 % 10
m = (t1 % 60) + 100
m0 = m % 10
m1 = m // 10 % 10
print(f"{h1}{h0}:{m1}{m0}")
