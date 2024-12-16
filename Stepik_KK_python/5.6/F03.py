"""
На вход программе подается натуральное число n. Необходимо его прочитать
и найти все простые числа (нацело делятся только на 1 и на себя), которые
меньше числа n, то есть, в диапазоне [2; n). Результат вывести на экран
в строчку через пробел.
"""

n = int(input())

for i in range(2, n):
    for j in range(2, i // 2 + 1):
        if not (i % j):
            break
    else:
        print(i, end=" ")
