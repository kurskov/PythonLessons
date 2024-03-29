"""Хвост

В семействе операционных систем Linux существует одна прекрасная
консольная утилита — tail. Она предназначена для случаев,
когда нам не нужно читать весь файл, а достаточно просмотреть
только несколько последних строк.

Напишите аналог этой утилиты.

Формат ввода
Пользователь вводит имя файла (F), а затем количество строк (N),
которые он хочет увидеть.

Формат вывода
Выведите N последних строк файла F.
"""

file_name = input()

text = []
with open(file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()

str_count = int(input())

for line in lines[(len(lines) - str_count) :]:
    print(line.rstrip("\n"))
