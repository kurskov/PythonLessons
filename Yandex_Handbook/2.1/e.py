"""Магазин

Кроме черешни в магазине продаётся множество других товаров,
которые продаются на развес.
Давайте автоматизируем расчёт сдачи и для них!

Формат ввода
Три натуральных числа:
 - цена товара;
 - вес товара;
 - количество денег у пользователя.

Формат вывода
Одно целое число — сдача, которую требуется отдать пользователю.
"""

price = int(input())
weight = int(input())
money = int(input())
print(money - price*weight)
