x = input()
ls = len(x)
x = int(x)
answer = "YES"

for i in range(1, int(ls / 2 + 1)):
    x1 = (x // (10 ** (i - 1))) % 10
    x2 = (x // (10 ** (ls - i))) % 10

    if x1 != x2:
        answer = "NO"

print(answer)
