"""
На вход программе подается натуральное число N. Необходимо его прочитать
и сгенерировать вложенный список с помощью list comprehension, размером N x N,
где первая строка содержала бы все нули, вторая - все единицы,
третья - все двойки и так до N-й строки. Результат вывести в виде таблицы
чисел как показано в примере ниже.
"""

n = int(input())

mtx = [[i] * n for i in range(n)]

[print(*row) for row in mtx]
