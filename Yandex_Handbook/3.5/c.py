"""Без комментариев 2.0

Как вы помните, когда вы комментируете свой код,
перед его выполнением интерпретатор удаляет комментарии.
Напишите программу, которая выполняет данную функцию за интерпретатор.

Формат ввода
Вводятся строки программы.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не нужно.
"""

from sys import stdin

text = []
for line in stdin:
    for index, symbol in enumerate(line):
        if symbol == "#":
            if index == 0:
                break
            quotes = line[:index].count('"')
            if quotes % 2 == 0:
                text.append(line[:index])
                break
        if index == len(line) - 1:
            text.append(line[:-1])

for str in text:
    print(str)
