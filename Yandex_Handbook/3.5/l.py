"""Разделяй и властвуй

Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:

    числа с преобладающим количеством чётных цифр;
    числа с преобладающим количеством нечётных цифр;
    числа с одинаковым количеством чётных и нечётных цифр.

Формат ввода
Пользователь вводит четыре имени файла.
Первый файл содержит произвольное количество чисел,
разделённых пробелами и символами перевода строки.

Формат вывода
В три другие файла выведите числа, которые подходят под требуемое условие.
Сохраните положение чисел в строках."""

import re

input_file_name = input()
even_file_name = input()
odd_file_name = input()
eq_file_name = input()

with open(input_file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()

even, odd, eq = "", "", ""
for line in lines:
    numbers = list(line.rstrip("\n").split())
    even_nums, odd_nums, eq_nums = [], [], []
    for number in numbers:
        full_lenght = len(number)
        even_lengnt = len(re.sub(r'([13579])', '', number))
        if full_lenght - even_lengnt < even_lengnt:
            even_nums.append(number)
        elif full_lenght - even_lengnt > even_lengnt:
            odd_nums.append(number)
        else:
            eq_nums.append(number)
    even += " ".join(even_nums) + "\n"
    odd += " ".join(odd_nums) + "\n"
    eq += " ".join(eq_nums) + "\n"

with open(even_file_name, "w", encoding="UTF-8") as file_output:
    file_output.writelines(even)
with open(odd_file_name, "w", encoding="UTF-8") as file_output:
    file_output.writelines(odd)
with open(eq_file_name, "w", encoding="UTF-8") as file_output:
    file_output.writelines(eq)
