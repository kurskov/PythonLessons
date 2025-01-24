"""
На вход программе подается строка со списком оценок, например:

2 неудовлетворительно удовлетворительно хорошо отлично

Первая цифра - это числовое значение первой оценки. Остальные оценки имеют возрастающие числа на 1.

Необходимо прочитать эту строку и с помощью генератора словарей сформировать словарь d,
в котором ключами будут выступать числа, а значениями - слова.
Например:

d = {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}

Вывести на экран значение сформированного словаря с ключом 4 (полагается, что такой ключ всегда существует).
"""

start, *marks = input().split()

d = {key: mark for key, mark in enumerate(marks, int(start))}

print(d[4])