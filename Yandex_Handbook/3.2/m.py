"""
Дайте чего-нибудь новенького!

Главный повар детского сада хочет приготовить в праздничный день блюда,
которые ни разу не готовил на этой неделе.
В его распоряжении есть список блюд:

    которые можно приготовить в столовой сегодня;
    которые были приготовлены в каждый из дней недели.

Формат ввода
Число блюд (N), которые можно приготовить в столовой.
N строк с названиями блюд. Число дней (M), о которых имеется информация.
M блоков строк для каждого из списков.
В первой строке каждого блока записано число блюд в заданный день,
затем перечисляются эти блюда.

Формат вывода
Список блюд, которые ещё не готовились на этой неделе в алфавитном порядке.
Если все возможные блюда уже были приготовлены, следует вывести
«Готовить нечего».
"""

n = int(input())
can_cooking = set()
for i in range(n):
    can_cooking.add(input())

m = int(input())
was_cooking = set()
for i in range(m):
    in_day = int(input())
    for j in range(in_day):
        was_cooking.add(input())

menu = can_cooking - was_cooking
if len(menu) != 0:
    menu = list(menu)
    menu.sort()
    for item in menu:
        print(item)
else:
    print("Готовить нечего")
