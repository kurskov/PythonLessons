"""
На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку
выбором полученного списка по возрастанию (неубыванию).
"""

lst = list(map(int, input().split()))

for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(*lst)