n = int(input())
value = ""

for i in range(n):
    x = int(input())
    max_ch = 0
    while x > 0:
        ch = x % 10
        x //= 10
        if ch > max_ch:
            max_ch = ch
    value += str(max_ch)

print(value)
