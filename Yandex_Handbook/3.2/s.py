"""
Частная собственность

Ребята приносят игрушки в детский сад и играют все вместе.
Сегодня они решили выяснить, игрушки какого типа принадлежат только одному
из детей. Напишите программу, которая по списку детей и их игрушек определит
«частную собственность».

Формат ввода
В первой строке задается количество детей в группе (N).
В каждой из следующих N строк записано имя ребенка и его игрушки в формате:
Имя: игрушка1, игрушка2, ....

Формат вывода
Список игрушек, которые есть только у одного из детей в алфавитном порядке.
"""

n = int(input())

all_toys = dict()
for i in range(n):
    text = input()
    text = text.split(": ")
    toys = list(set(text[1].split(", ")))
    for toy in toys:
        if toy in all_toys:
            all_toys[toy] += 1
        else:
            all_toys[toy] = 1

private_toys = list()
for toy in all_toys:
    if all_toys[toy] == 1:
        private_toys.append(toy)

private_toys.sort()

for toy in private_toys:
    print(toy)
