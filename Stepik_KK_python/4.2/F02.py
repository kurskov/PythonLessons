"""
На вход программе подаются три целых числа, записанных в одну строку
через пробел. Необходимо прочитать их и определить наименьшее среди
прочитанных чисел. Наименьшее найденное значение вывести на экран.

P.S. Программу реализовать следует, используя условный оператор,
без использования функции min.
"""

a, b, c = map(int, input().split())

if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

print(a)
