"""
На вход программе подается строка. Необходимо ее прочитать и найти в ней
все индексы строкового фрагмента "ра". Выведите найденные индексы на экран
в одну строчку через пробел. Если же фрагмент "ра" отсутствует в строке,
то вывести -1.
"""

s = input().lower()

lst, i = [], -1
while (i := s.find("ра", i + 1)) > -1:
    lst.append(i)

print(*lst or [-1])
