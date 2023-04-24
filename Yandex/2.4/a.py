n = int(input())

for i in range(1, n + 1):
    s = str(i)
    for j in range(2, n + 1):
        s += " " + str(j * i)
    print(s)
