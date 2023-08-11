"""Файловая статистика 2.0

Напишите программу, которая для заданного файла вычисляет следующие
параметры:

    количество всех чисел;
    количество положительных чисел;
    минимальное число;
    максимальное число;
    сумма всех чисел;
    среднее арифметическое всех чисел с точностью до двух знаков после
    запятой.

Формат ввода

Пользователь вводит два имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами
и символами перевода строки.
Формат вывода

Выведите статистику во второй файл в формате JSON.

Ключи значений задайте соответственно:

    count — количество всех чисел;
    positive_count — количество положительных чисел;
    min — минимальное число;
    max — максимальное число;
    sum — сумма всех чисел;
    average — среднее арифметическое всех чисел с точностью до двух знаков
    после запятой.
"""

from statistics import mean
import json

input_file_name = input()
output_file_name = input()

numbers = []
with open(input_file_name, encoding="UTF-8") as file_input:
    lines = file_input.readlines()
    for line in lines:
        numbers.extend(list(map(int, line.rstrip("\n").split())))

stats = {"count": len(numbers),
         "positive_count": len([num for num in numbers if num > 0]),
         "min": min(numbers),
         "max": max(numbers),
         "sum": sum(numbers),
         "average": str(round(mean(numbers), 2))}

with open(output_file_name, "w", encoding="UTF-8") as file_output:
    json.dump(stats, file_output, indent=4)
