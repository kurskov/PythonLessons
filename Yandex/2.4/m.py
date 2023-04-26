"""
Задача M. Числовой прямоугольник 2.0

Давайте вновь поможем воспитательнице учить ребят числам. 
Напишите программу, которая строит числовой прямоугольник требуемого размера.

Формат ввода
В первой строке записано число N — высота числового прямоугольника.  
Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированный числовой прямоугольник требуемого размера.  
Чтобы прямоугольник был красивым, каждый его столбец должен обладать одинаковой шириной.
"""

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
