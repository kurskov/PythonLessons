"""
На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку
полученного списка по возрастанию (неубыванию) методом всплывающего пузырька.
"""

lst = list(map(int, input().split()))

for n in range(len(lst) - 1):
    for i in range(0, len(lst) - 1 - n):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(*lst)
