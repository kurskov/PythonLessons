n = int(input())
ans = 0

for i in range(1, n + 1):
    x = input()
    ls = len(x)
    x = int(x)
    for j in range(ls):
        ans += (x // (10 ** j)) % 10

print(ans)
