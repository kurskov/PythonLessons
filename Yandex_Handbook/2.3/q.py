x = input()
ls = len(x)
x = int(x)
answer = ""

for i in range(1, ls + 1):
    n = (x // (10 ** (i - 1))) % 10
    if n % 2 != 0:
        answer = str(n) + answer

print(answer)
