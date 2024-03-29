"""
Спортивные гадания

Хорошо, спортсмены расставлены на старте. Вот только угадать
финалистов практически невозможно. Давайте напишем программу,
которая выводит список возможных победителей.

Формат ввода
В первой строке задано натуральное число N — количество спортсменов.
В следующих N строках записаны имена спортсменов.

Формат вывода
Отсортированный по алфавиту список вариантов.
Имена в каждой строке выводить через запятую и пробел.
"""

from itertools import permutations

n = int(input())
names = [input() for i in range(n)]
starts = list(permutations(sorted(names), 3))

for start in starts:
    print(", ".join(start))
