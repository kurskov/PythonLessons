"""
Символическая разница

А ещё в промышленных задачах часто требуется находить общее среди
данных, полученных из раных источников. Напишите программу, которая
по двум строкам определяет их общие символы.

Формат ввода
Вводится две строки.

Формат вывода
Требуется вывести все символы этой строки без повторений.
Порядок вывода не имеет значения.
"""

text1 = set(input())
text2 = set(input())

common = text1 & text2

for letter in common:
    print(letter, end="")
