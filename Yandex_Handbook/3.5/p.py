"""Найдётся всё 3.0

Давайте вновь напишем небольшой компонент поисковой системы.

Формат ввода
Сначала вводится поисковый запрос.
Затем вводятся имена файлов, среди которых следует произвести поиск.

Формат вывода
Выведите все имена файлов, в которых есть поисковая строка без учета
регистра и повторяющихся пробельных символов.
Если ни в одном файле информация не была найдена, выведите "404. Not Found".

Примечание
Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b",
"a b" и "a\nb" как одинаковые.
"""

from sys import stdin

is_find = False

input = []
for line in stdin:
    input.append(line.rstrip())

request = input.pop(0).lower()

for file_name in input:
    file_content = ""

    with open(file_name, encoding="UTF-8") as file_input:
        lines = file_input.readlines()

    for line in lines:
        line = " ".join(line.lower().split())
        if line != "":
            file_content += line + " "

    if file_content.count(request):
        print(file_name)
        is_find = True

if not is_find:
    print("404. Not Found")
