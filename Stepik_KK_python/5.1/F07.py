"""
На вход программе подается натуральное число (то есть,
целое положительное) от трехзначного и более. Необходимо прочитать
это число и найти произведение всех его цифр. Результат (произведение)
вывести на экран. Программу реализовать при помощи цикла while.
"""

lst = list(map(int, input()))

p = 1
while lst:
    p *= lst.pop()

print(p)
