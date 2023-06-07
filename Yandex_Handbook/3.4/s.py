"""
Таблица истинности 2

Продолжим работу с таблицами истинности. Продумайте программу,
которая для введённого сложного логического высказывания строит
таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное
для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
В выражении все переменные заданы заглавными латинскими буквами.
Обратите внимание на параметры __globals и __locals у функции eval.
"""

expression = input()

abc = set()
exp_list = list(expression)
for symbol in exp_list:
    if symbol.isupper():
        abc.add(symbol)
abc = sorted(list(abc))

print(" ".join(abc) + " F")

vars = dict()
for i in range(2 ** len(abc)):
    conditions = list(bin(i)[2:].zfill(len(abc)))
    print(" ".join(conditions), end=" ")
    for j in range(len(abc)):
        vars[abc[j]] = int(conditions[j])
    print("%i" % eval(expression, vars))
