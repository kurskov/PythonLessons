"""В ожидании доставки

Сегодня в N часов M минут хозяин магазина заказал доставку нового товара.
Оператор сказал, что продукты доставят через T минут.
Сколько будет времени на электронных часах, когда привезут
долгожданные продукты?

Формат ввода
В первой строке записано натуральное число N (0≤N<24).
Во второй строке записано натуральное число M (0≤M<60).
В третьей строке записано натуральное число T (30≤T<10^9).

Формат вывода
Одна строка, представляющая циферблат электронных часов.
"""

n = int(input())
m = int(input())
t = int(input())
time = n * 60 + m + t
h = time // 60 % 24
m = time % 60
print(f"{h // 10}{h % 10}:{m // 10}{m % 10}")
