"""
Найдётся всё

Поиск информации — одна из основных нужд в современном мире.
Создайте программу, которая реализует маленький компонент поисковой системы.

Формат ввода
Вводится натуральное число N — количество страниц, среди которых требуется произвести поиск.
В каждой из последующих N строк записаны заголовки страниц.
В последней строке записан поисковый запрос.

Формат вывода
Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
Порядок заголовков должен сохраниться.
"""

n = int(input())

text = []
for i in range(n):
    text.append(input())

search = input()

for str in text:
    if str.lower().find(search.lower()) > -1:
        print(str)
