n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        s = str(j) + " * " + str(i) + " = " + str(j * i)
        print(s)
