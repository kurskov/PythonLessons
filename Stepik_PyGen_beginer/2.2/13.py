"""Повторяй за мной

Напишите программу, которая считывает три строки по очереди,
а затем выводит их в той же последовательности, каждую на отдельной строчке.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные строки в той же последовательности,
каждую на отдельной строке.

Примечание 1.
Для считывания текста используйте команду input(),
для печати текста на экране используйте команду print().

Примечание 2.
Не используйте никакой текст и никакие другие аргументы
внутри функции input(), т.к. это повлияет на вывод и ваша
программа не пройдёт тесты.
"""

print(input(), input(), input(), sep="\n")
