x = int(input())
answer = 0

while x != 0:
    v = x % 10
    if v > answer:
        answer = v
    x = x // 10

print(answer)
