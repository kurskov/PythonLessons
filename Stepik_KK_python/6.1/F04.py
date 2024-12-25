"""
На вход программе поступают данные в виде набора строк в формате:

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). В программе уже
реализовано считывание всех строк и сохранение их в виде списка:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Необходимо преобразовать список lst_in в словарь d (без использования
функции dict()) и вывести полученный словарь на экран командой:

print(*sorted(d.items()))
"""

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {int(key): value for key, value in [s.split("=") for s in lst_in]}

print(*sorted(d.items()))
