"""Три последовательных числа

Напишите программу вывода на экран трех последовательно идущих чисел,
каждое на отдельной строке. Первое число вводит пользователь,
остальные числа вычисляются в программе.

Формат входных данных
На вход программе подается одно целое число.

Формат выходных данных
Программа должна вывести три последовательно идущих числа
в соответствии с условием задачи.

Примечание.
Не используйте никакой текст и никакие другие аргументы внутри
функции input(), т.к. это повлияет на вывод и ваша программа
не пройдёт тесты.
"""

start = int(input())
print(start, start + 1, start + 2, sep="\n")
