"""
На вход программе подаются целые числа, записанные в одну строку через пробел. Необходимо их прочитать и сохранить
в кортеже. Затем, создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа.
Уникальные числа должны следовать в том же порядке, что и в исходном кортеже. Отобразите найденные уникальные числа
в одну строчку через пробел.

P. S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве практики пока обойдемся без них.
"""

nums = tuple(map(int, input().split()))

t = tuple(dict.fromkeys(nums))

print(*t)