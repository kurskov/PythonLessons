"""
Треугольник Паскаля
"""

n = int(input("Введите количество строк: "))

TP = [[1] * (i + 1) for i in range(n)]

for row in range(n):
    for cell in range(1, row):
        TP[row][cell] = TP[row - 1][cell - 1] + TP[row - 1][cell]

width = len(' '.join(map(str, TP[-1])))

print(*[f"{" ".join(map(str, line)):^{width}}" for line in TP], sep="\n")
