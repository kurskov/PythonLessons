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
    pos = line.find("# ")
    if pos < 0:
        text.append(line)
    elif pos > 0:
        quotes = line[:pos].count('"')
        if quotes % 2 == 0:
            text.append(line[:pos])

for str in text:
    print(str)
