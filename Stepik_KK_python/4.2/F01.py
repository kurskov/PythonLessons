"""
Объявите в программе следующую многострочную переменную (меню):

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

Эту строку можно разбить на отдельные строки,
если вы видите в этом необходимость.

Далее, на вход программы подается целое число от 1 до 6.
Необходимо его прочитать и вывести пункт меню, связанный с этим числом.
Реализовать программу с использованием операторов if-elif
"""

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

item = int(input())

if item < 6:
    next_item = str(item + 1)
    print(m[m.index(str(item)):m.index(str(next_item))])

elif item == 6:
    print(m[m.index(str(item)):])
