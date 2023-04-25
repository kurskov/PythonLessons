n = int(input())
m = int(input())

col = len(str(n * m))
current = 0

for i in range(1, n + 1):
    row = ""
    for j in range(1, m + 1):
        current += 1
        text = str(current)
        while len(text) < col:
            text = " " + text
        if i % 2 == 0:
            if j == 1:
                row = text + row
            else:
                row = text + " " + row
        else:
            if j == m:
                row += text
            else:
                row += text + " "
    print(row)
