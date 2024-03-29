"""
А роза упала на лапу Азора

Существуют такое интересное понятие как палиндром — число,
слово, предложение и так далее, которое и слева-направо,
и справа-налево читается одинаково.

Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода
Одно четырёхзначное число

Формат вывода
YES если число является палиндромом, иначе — NO.
"""

val = int(input())

v0 = val % 10
v1 = val // 10 % 10
v2 = val // 100 % 10
v3 = val // 1000 % 10

if (str(v3) + str(v2)) == (str(v0) + str(v1)):
    print("YES")
else:
    print("NO")
