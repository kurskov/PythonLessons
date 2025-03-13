from math import inf


def one_to_many(list_in: list, list_out=[]) -> list:
    """
    Разбиваем список чисел на список списков.
    С рекурсией )
    """
    if list_in:
        list_out.append([list_in.pop()])
        one_to_many(list_in, list_out)
    return list_out


def sorted_to_list(list_1: list, list_2: list) -> list:
    """
    Собираем из двух отсортированных списков чисел
    один отсортированный список чисел
    С итераторами )
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
    Собираем из списка списков отсортированный список
    """
    list_out = []
    a = len(list_in)
    if len(list_in) > 1:
        list_odd = list_in[::2]
        list_even = list_in[1::2]
        for i in range(len(list_even)):
            list_out.append(sorted_to_list(list_odd[i], list_even[i]))
        if len(list_in) % 2:
            list_out.append(list_odd[-1])
        print(list_out)
        return many_to_one(list_out)


nums = list(map(int, input().split()))

print(one_to_many(nums))
print(many_to_one(one_to_many(nums)))
