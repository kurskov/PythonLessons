"""Повторяй за мной 2

Напишите программу, которая считывает три строки по очереди,
а затем выводит их в обратной последовательности, каждую
на отдельной строчке.

Формат входных данных
На вход программе подается три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные строки в обратной последовательности,
каждую на отдельной строке.

Примечание 1.
Используйте 3 переменные для сохранения введённых строк текста.

Примечание 2.
Не используйте никакой текст и никакие другие аргументы внутри
функции input(), т.к. это повлияет на вывод и ваша программа
не пройдёт тесты.
"""

a, b, c = input(), input(), input()
print(c, b, a, sep="\n")