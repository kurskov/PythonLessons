"""Файловая разница

Напишите программу, которая определяет, какие слова есть только
в одном из файлов.

Формат ввода
Пользователь вводит три имени файлов.
Каждый из входных файлов содержит произвольное количество слов,
разделённых пробелами и символами перевода строки.

Формат вывода
В третий файл выведите в алфавитном порядке без повторений список слов,
которые есть только в одном из файлов.
"""

first_file_name = input()
second_file_name = input()
answer_file_name = input()

first_words = set()
with open(first_file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()
    for line in lines:
        wodrs_in_line = set(line.rstrip("\n").split())
        first_words |= wodrs_in_line

second_words = set()
with open(second_file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()
    for line in lines:
        wodrs_in_line = set(line.rstrip("\n").split())
        second_words |= wodrs_in_line

lines = []
for word in sorted(first_words ^ second_words):
    lines.append(word + "\n")

with open(answer_file_name, "w", encoding="UTF-8") as file_output:
    file_output.writelines(lines)
