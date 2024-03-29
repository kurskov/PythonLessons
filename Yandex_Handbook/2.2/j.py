"""
Лучшая защита — шифрование

Коля испугался, что Аня подсмотрит все его пароли в блокноте,
и решил их зашифровать. Для этого он берёт изначальный пароль —
трёхзначное число — и по нему строит новое число по следующим правилам:

- находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
- находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
- Эти две суммы, записанные друг за другом, в порядке не возрастания,
формируют новое число.

Помогите реализовать алгоритм шифрования.

Формат ввода
Одно трёхзначное число

Формат вывода
Результат шифрования
"""

n = int(input())

n0 = n % 10
n1 = n // 10 % 10
n2 = n // 100 % 10

s1 = n0 + n1
s2 = n1 + n2

if s1 >= s2:
    print(f"{s1}{s2}")
else:
    print(f"{s2}{s1}")
