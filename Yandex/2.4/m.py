n = int(input())
m = int(input())

col = len(str(n * m))

for i in range(1, n + 1):
    row = ""
    current = i
    for j in range(1, m + 1):
        text = str(current)
        while len(text) < col:
            text = " " + text
        if j == m:
            row += text
        else:
            row += text + " "
        current += n
    print(row)
