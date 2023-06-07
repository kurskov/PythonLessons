"""
Таблицы истинности 3

Продолжим работу с таблицами истинности.
К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
Самые частые не стандартные операции это: импликация, строгая дизъюнкция
и эквивалентность.

Обозначим их следующим образом:

    импликация — ->;
    строгая дизъюнкция — ^;
    эквивалентность — ~.

Напишите программу, которая для введённого сложного логического
высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

    Заглавная латинская буква — переменная;
    not — отрицание;
    and — конъюнкция;
    or — дизъюнкция;
    ^ — строгая дизъюнкция;
    -> — импликация;
    ~ — эквивалентность;
    () — логические скобки.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
Прежде, чем реализовывать новые операции, обратите внимание на их приоритет.
Рекомендуем воспользоваться знаниями полученными при решении задачи
«Польский калькулятор».
"""

expression = input()

# выбираем список переменных
abc = set()
exp_symbols = list(expression)
for symbol in exp_symbols:
    if symbol.isupper():
        abc.add(symbol)
abc = sorted(list(abc))
print(" ".join(abc) + " F")

# заменяем в строке неизвестные функции
exp_items = expression.split()
for i in range(len(exp_items)):
    match exp_items[i]:
        case "^":
            exp_items[0] = "(" + exp_items[0]
            exp_items[i] = ") != ("
            exp_items[len(exp_items) - 1] += ")"
        case "->":
            exp_items[i] = "<="
        case "~":
            exp_items[0] = "(" + exp_items[0]
            exp_items[i] = ") == ("
            exp_items[len(exp_items) - 1] += ")"
expression = " ".join(exp_items)

# собираем таблицу истинности
vars = dict()
for i in range(2 ** len(abc)):
    conditions = list(bin(i)[2:].zfill(len(abc)))
    print(" ".join(conditions), end=" ")
    for j in range(len(abc)):
        vars[abc[j]] = int(conditions[j])
    print("%i" % eval(expression, vars))

print(expression)
