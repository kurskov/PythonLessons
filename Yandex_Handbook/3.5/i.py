"""Файловая чистка

Python в первую очередь скриптовый язык. Такие языки часто используются
для создания консольных утилит.

Напишите простую утилиту, которая очищает заданный файл от:

    повторяющихся пробелов;
    повторяющихся символов перевода строки;
    табуляций,
    излишних пробелов в начале и конце строк.

Формат ввода

Пользователь вводит два имени файлов.
Входной файл содержит неформатированный текст произвольной длины.
Формат вывода

Во второй файл выведите очищенный текст.
"""

first_file_name = input()
second_file_name = input()

with open(first_file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()

output = []
for line in lines:
    line = line.replace("\t", "")
    line = " ".join(line.split())
    if line != "":
        output.append(line + "\n")

with open(second_file_name, "w", encoding="UTF-8") as file_output:
    file_output.writelines(output)
