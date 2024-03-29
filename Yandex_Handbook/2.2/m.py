"""
Властелин Чисел: Братство общей цифры

Во времена магии и драконов существовало мнение, что числа
обладают великой силой, способной изменить мир.
Всё началось с написания великих чисел. Три числа были
переданы эльфам. Семь — отданы повелителям гномов.
А девять... были переданы человеческому роду.
Но все они оказались обмануты, потому что существовало ещё одно число.
В стране Нумия на бумаге из тёмного папируса властелин Зерон тайно
написал Единую Цифру, подчиняющую себе все великие числа.
Давайте выясним, что это за цифра.

Формат ввода
В первой строке записано двузначное число одного из эльфов.
Во второй строке — Гномов.
В третьей — Людей.

Формат вывода
Одна цифра — общая у всех трёх чисел в одинаковой позиции
"""

v1 = int(input())
v2 = int(input())
v3 = int(input())

if (v1 % 10) == (v2 % 10) == (v3 % 10):
    print(v1 % 10)

if (v1 // 10 % 10) == (v2 // 10 % 10) == (v3 // 10 % 10):
    print(v1 // 10 % 10)
