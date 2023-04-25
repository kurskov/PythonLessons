n = int(input())
win = ""
value = 0

for i in range(n):
    name = input()
    x = int(input())
    val = 0
    while x > 0:
        val += x % 10
        x //= 10
    if val >= value:
        value = val
        win = name

print(win)
