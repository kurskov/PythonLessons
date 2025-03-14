"""
На вход программе подаются данные в формате ключ=значение, записанные
через пробел. Значениями здесь являются целые числа (см. пример ниже).
Необходимо прочитать строку с этими данными и на их основе сформировать
словарь d, используя функцию dict(). Результирующий словарь вывести
на экран командой:

print(*sorted(d.items()))
"""

lst = input().split()

d = dict([[key, int(value)] for key, value in [s.split("=") for s in lst]])

print(*sorted(d.items()))
