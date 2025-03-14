"""
На вход программе подаются целые числа, записанные через пробел.
Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку этого списка
по возрастанию с помощью алгоритма сортировки слиянием.
Функция должна возвращать новый отсортированный список.

Вызовите результирующую функцию сортировки для введенного списка и отобразите результат
на экран в виде последовательности чисел, записанных через пробел.

Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.

P. S. Теория сортировки в видео предыдущего шага.
"""
from math import inf


def one_to_many(list_in: list, list_out=[]) -> list:
    """
    Разбиваем список чисел на список списков.
    С рекурсией )
    :param list_in: Исходный список чисел
    :param list_out: Вспомогательный пустой список, при вызове не используется
    :return: Список списков единичной длины, в каждом из которых по одному числу исходного списка
    """
    if list_in:
        list_out.append([list_in.pop()])
        one_to_many(list_in, list_out)

    return list_out


def sorted_to_list(list_1: list, list_2: list) -> list:
    """
    Собираем из двух отсортированных списков чисел один отсортированный список чисел.
    С итераторами )
    :param list_1: Первый отсортированный список
    :param list_2: Второй отсортированный список
    :return: Результирующий отсортированный список, содержащий все значения первого и второго списка
    """
    res = []
    iter_1, iter_2 = iter(list_1), iter(list_2)

    a, b = next(iter_1), next(iter_2)
    for _ in range(len(list_1) + len(list_2)):
        if a < b:
            res.append(a)
            a = next(iter_1, inf)
        else:
            res.append(b)
            b = next(iter_2, inf)

    return res


def many_to_one(list_in: list) -> list:
    """
    Собирает из списка списков отсортированный список.
    С рекурсией )
    :param list_in: Список списков единичной длины
    :return: Список единичной длины с отсортированным списком
    """
    if len(list_in) <= 1:
        return list_in

    list_odd = list_in[::2]
    list_even = list_in[1::2]
    list_out = []

    for i in range(len(list_even)):
        list_out.append(sorted_to_list(list_odd[i], list_even[i]))

    if len(list_in) % 2:
        list_out.append(list_odd[-1])

    return many_to_one(list_out)


def new_sorted(list_in: list) -> list:
    """
    Сортирует значения списка в порядке возрастания
    :param list_in: Список для сортировки
    :return: Отсортированный список
    """
    if list_in:
        return many_to_one(one_to_many(list_in))[0]
    return []


nums = list(map(int, input().split()))

print(*new_sorted(nums))
