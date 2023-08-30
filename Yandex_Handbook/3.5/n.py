"""Слияние данных

Одна местная компания производит обновление данных о пользователях
и заодно решили реорганизовать систему хранения.

Напишите программу, которая обновляет данные о пользователях,
записанных в JSON файле.

Формат ввода
Пользователь вводит два имени файла.
В первом хранится JSON массив пользователей.
Во втором — массив новых данных.
Информация о каждом пользователе представляется JSON объектом,
в котором обязательно присутствует поле name, описывающее имя пользователя.
Остальные поля являются дополнительными.

Формат вывода
В первый файл запишите информацию о пользователях в виде JSON объекта,
ключами которого выступают имена пользователей, а значениями — объекты
с информацией о них.

Если какая-либо дополнительная информация о пользователе изменяется,
то требуется сохранить лексикографически большее значение.
"""

import json

users_file_name = input()
updates_file_name = input()

with open(users_file_name, encoding="UTF-8") as file_input:
    users = json.load(file_input)

with open(updates_file_name, encoding="UTF-8") as file_input:
    updates = json.load(file_input)

result = dict()
for user in users:
    result[user.pop("name")] = user

for update in updates:
    name = update.pop("name")
    for key, value in update.items():
        result[name][key] = max(result[name].get(key, ""), value)

with open(users_file_name, "w", encoding="UTF-8") as file_output:
    json.dump(result, file_output, ensure_ascii=False, indent=4)
