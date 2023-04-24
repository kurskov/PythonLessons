n = int(input())
num = -1
h0 = 0

for i in range(n):
    b = int(input())
    h = b % 256
    r = int(((b - h) % (256 ** 2)) // 256)
    m = int((b - h - (r * 256)) // 256 ** 2)
    if (num < 0) and ((h >= 100) or (h != (((m + r + h0) * 37) % 256))):
        num = i
    h0 = h

print(num)
