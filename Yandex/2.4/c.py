n = int(input())
stop = False
v = 1

for i in range(1, n + 1):
    s = ""
    for j in range(1, i + 1):
        if s == "":
            s += str(v)
        else:
            s += " " + str(v)
        v += 1
        if v > n:
            stop = True
            break
    print(s)
    if stop:
        break
