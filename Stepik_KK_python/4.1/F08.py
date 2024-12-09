"""
На вход программе подаются четыре целых числа a, b, c, d, записанных
в одну строку через пробел. Необходимо прочитать эти числа и определить,
войдет ли в конверт с внутренними размерами a и b мм (первые два числа)
прямоугольная открытка с размерами с и d мм (следующие два числа).
Для размещения открытки в конверте необходим зазор в 1 мм с каждой стороны.
Открытку можно поворачивать на 90 градусов.
Вывести "ДА", если открытка входит, и "НЕТ" в противном случае.
"""

numbers = map(int, input().split())

a, b = sorted(numbers[:2])
c, d = sorted(numbers[2:])

print(('НЕТ', 'ДА')[a >= c + 2 and b >= d + 2])