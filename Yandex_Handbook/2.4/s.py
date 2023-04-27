"""
Числовой квадрат

К сожалению, и змейки детям надоели, поэтому воспитательнице нужна новая программа. 
Напишите программу, которая строит числовой квадрат требуемого размера.

Формат ввода
В первой строке записано число N — высота и ширина числового квадрата.

Формат вывода
Требуется вывести сформированный числовой квадрат требуемого размера.
Чтобы квадрат был красивым, каждый его столбец — одинаковой ширины.
"""

n = int(input())
border = int(n / 2)

for i in range(-border, border + 1):
    if i != 0 or (i == 0 and n % 2 != 0):
        row = ""
        for j in range(-border, border + 1):
            if j != 0 or (j == 0 and n % 2 != 0):
                value = str(min(border - abs(i) + 1, border - abs(j) + 1))
                target_width = len(str(border + 1))
                while len(value) < target_width:
                    value = " " + value
                row += value
                if j < border:
                    row += " "
        print(row)