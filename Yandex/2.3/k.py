x = int(input())
summa = 0

while x != 0:
    summa += x % 10
    x = x // 10

print(summa)
