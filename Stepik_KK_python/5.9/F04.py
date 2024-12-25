"""
Повторите задачу с транспонированием прямоугольной матрицы с помощью
list comprehension, изложенной в видео-уроке к этой практике. На вход
программе поступает таблица целых чисел, чтение которой уже реализовано
в программе:

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

Нужно транспонировать список lst_in (строки заменяются на столбцы) и результат
сохранить в списке A. Отобразите полученный список A с помощью следующей
конструкции:

for row in A:
    print(*row)

Желательно сделать эту задачу не пересматривая видео.
"""

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]

for row in A:
    print(*row)
