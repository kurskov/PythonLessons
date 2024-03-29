"""
Зайка — 8

Продолжаем считать заек за окном поезда.

Формат ввода
В первой строке записано натуральное число N — количество
выделенных придорожных местностей.
В каждой из N последующих строк записано описание придорожной местности.

Формат вывода
Вывести все найденные объекты в придорожных местностях.
"""

n = int(input())
words = []

for i in range(n):
    text = input()
    words += text.split()

words = set(words)

for word in words:
    print(word)
