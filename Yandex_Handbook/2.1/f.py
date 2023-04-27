"""
Чек

Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.

Формат ввода
    название товара;
    цена товара;
    вес товара;
    количество денег у пользователя.

Формат вывода
Чек
<название товара> - <вес>кг - <цена>руб/кг
Итого: <итоговая стоимость>руб
Внесено: <количество денег от пользователя>руб
Сдача: <сдача>руб
"""

name = str(input())
price = int(input())
weight = int(input())
money = int(input())
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {weight * price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - (weight * price)}руб")
