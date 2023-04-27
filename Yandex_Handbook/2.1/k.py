"""
Автоматизация игры

Всё в том же детском саду ребята очень любят играть с цифрами.
Одна из таких игр — перестановка цифр четырёхзначного числа.
Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.

Формат ввода
Одно четырёхзначное число.

Формат вывода
Одно четырёхзначное число — результат перестановки.
"""

n = int(input())
a = n // 1000 % 10
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(f"{b}{a}{d}{c}")
