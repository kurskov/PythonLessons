"""
Сборы на прогулку

Воспитатель в детском саду устал тратить время, чтобы построить детей по парам.
Он договорился с детьми, чтобы те делились на две,
по возможности равные, группы.
Напишите программу, которая по списку двух шеренг составляет пары детей.

Формат ввода
Вводится две строки с именами детей, записанными через запятую и пробел.

Формат вывода

Требуется вывести список пар, которые можно составить, если последовательно
брать из каждой шеренги по одному ребёнку.
Имена в парах выводить через дефис окружённый пробелами.

Примечание
В одной из групп может быть на одного ребенка больше, чем в другой.
Этот ребёнок при формировании пар не учитывается и идёт в паре с воспитателем.
"""

s1 = input().split(", ")
s2 = input().split(", ")

for pair in zip(s1, s2):
    print(pair[0], pair[1], sep=" - ")
