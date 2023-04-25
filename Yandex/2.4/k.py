n = int(input())
ans = 0

for i in range(n):
    x = int(input())
    simple = True
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            simple = False
            break
    if simple and (x != 1):
        ans += 1

print(ans)
