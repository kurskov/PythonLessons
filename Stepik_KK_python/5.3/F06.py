"""
На вход программе подается строка с названиями городов, записанных
в одну строчку через пробел. Необходимо прочитать эту строку и сформировать
список из названий городов. Затем, перебрать полученный список циклом for
и заменить названия городов на длины их строк. Результат вывести на экран
в виде последовательности чисел через пробел в одну строчку.
"""

cities = input().split()

for i in range(len(cities)):
    cities[i] = len(cities[i])

print(*cities)