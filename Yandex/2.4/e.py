n = int(input())
ans = 0

for i in range(1, n + 1):
    test = 0
    while True:
        text = input()
        if "зайка" in text:
            test += 1
        if "ВСЁ" in text:
            break
    if test > 0:
        ans += 1

print(ans)
