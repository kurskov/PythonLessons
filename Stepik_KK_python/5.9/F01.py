"""
На вход программе подается двумерная таблица из целых чисел (см. пример ниже).
В программе уже реализовано его чтение и сохранение в двумерном списке:

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

С помощью list comprehension необходимо преобразовать двумерный список lst_in
в одномерный так, чтобы значения элементов шли в обратном порядке.
Результат отобразить в виде строки из чисел, записанных через пробел.
"""

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst = [x
       for row in reversed(lst_in)
       for x in reversed(row)]

print(*lst)
