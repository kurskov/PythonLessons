"""
А и Б сидели на трубе

Сложение чисел весьма простая задача.
К сожалению, пользователи не всегда вводят данные так, как нам удобно.

Формат ввода
Два целых числа, разделённые пробелом.

Формат вывода
Одно целое число — сумма переданных чисел.
"""

text = input()
numbers = text.split()
sum = 0

for number in numbers:
    sum += int(number)

print(sum)
