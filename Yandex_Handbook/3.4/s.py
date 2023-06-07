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
abc = sorted(set(symbol for symbol in expression if symbol.isupper()))
print(" ".join(abc), "F")

vars = dict()
for i in range(2 ** len(abc)):
    conditions = list(bin(i)[2:].zfill(len(abc)))
    for j in range(len(abc)):
        vars[abc[j]] = int(conditions[j])
    print(" ".join(conditions), int(eval(expression, vars)))
