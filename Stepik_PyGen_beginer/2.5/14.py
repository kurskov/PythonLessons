"""Перестановка цифр

Дано трехзначное число abc, в котором все цифры различны.
Напишите программу, которая выводит шесть чисел, образованных
при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число,
все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке
цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cba.
"""

from itertools import permutations

a = input()
for i in permutations(a, len(a)):
    print("".join(i))
