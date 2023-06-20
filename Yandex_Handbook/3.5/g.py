"""Файловая статистика

Напишите программу, которая для заданного файла вычисляет следующие параметры:

    количество всех чисел;
    количество положительных чисел;
    минимальное число;
    максимальное число;
    сумма всех чисел;
    среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Формат ввода
Пользователь вводит имя файла.
Файл содержит произвольное количество чисел, разделённых пробелами
и символами перевода строки.

Формат вывода
Выведите статистику в указанном порядке.
"""

from statistics import mean

file_name = input()

numbers = []
with open(file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()
    for line in lines:
        numbers.extend(list(map(int, line.rstrip("\n").split())))

print(len(numbers))

print(len([num for num in numbers if num > 0]))

print(min(numbers))

print(max(numbers))

print(sum(numbers))

print("{:.2f}".format(mean(numbers)))
