"""
Однофамильцы — 2

Вновь поможем сотруднику из отдела кадров выяснить,
сколько мужчин-однофамильцев работает в организации,
но уже немного с иными условиями.

Формат ввода
В первой строке указывается количество мужчин — сотрудников организации (N).
Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.

Формат вывода
Список однофамильцев в организации с указанием их количества
в алфавитном порядке.
Если таковых нет — вывести «Однофамильцев нет».
"""

n = int(input())
men = dict()
counter = 0

for i in range(n):
    name = input()
    if name in men:
        men[name] += 1
    else:
        men[name] = 1

men = list(men.items())
men.sort()

for name in men:
    if name[1] > 1:
        print(f"{name[0]} - {name[1]}")
        counter += 1

if counter == 0:
    print("Однофамильцев нет")
