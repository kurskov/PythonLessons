"""
Кашееды — 3

Вернёмся к условию, когда каждый воспитанник детского сада любит либо манную,
либо овсяную, либо обе эти каши.
Напишите программу, которая позволит воспитателю узнать, какие дети любят
только одну кашу.

Формат ввода
В первых двух строках указывается количество детей, любящих манную и овсяную
каши (N и M).
Затем идут N+M — перемешанные фамилии детей.
Гарантируется, что в группе нет однофамильцев.

Формат вывода
В алфавитном порядке фамилии учеников, которые любят только одну кашу.
Если таких не окажется, в строке вывода нужно написать «Таких нет».
"""

n = int(input())
m = int(input())
names = set()

for i in range(n + m):
    name = input()
    if name in names:
        names.discard(name)
    else:
        names.add(name)

if len(names) == 0:
    print("Таких нет")
else:
    names = list(names)
    names.sort()
    for name in names:
        print(name)
