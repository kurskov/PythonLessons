"""Обновление данных

Часто приходится обновлять данные.

Создайте программу, которая обновляет JSON файл.

Формат ввода
Пользователь вводит имя файла.
Затем вводятся строки вида ключ == значение.

Формат вывода
В заданный пользователем файл следует записать обновленный JSON.
"""

from sys import stdin
import json

file_name = input()
with open(file_name, encoding="UTF-8") as file_input:
    records = json.load(file_input)

for line in stdin:
    text = line.rstrip("\n").split()
    records[text[0]] = text[2]

with open(file_name, "w", encoding="UTF-8") as file_output:
    json.dump(records, file_output, ensure_ascii=False, indent=4)
