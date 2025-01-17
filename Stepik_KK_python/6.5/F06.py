"""
На вход программе подаются две строки со списком городов, которые объехал Сергей
в 1-й и 2-й годы своего путешествия по России. Необходимо прочитать эти наборы
строк и сохранить их в отдельных списках (или кортежах). Затем, требуется определить,
включал ли его маршрут во 2-й год все города 1-го года путешествия? Если это так,
то вывести "ДА", иначе "НЕТ".
"""

cities1 = input().split()
cities2 = input().split()

print(("НЕТ", "ДА")[set(cities1) <= set(cities2)])
