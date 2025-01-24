"""
На вход программе подается список целых чисел, записанных в одну строчку
через пробел. Необходимо их прочитать и сохранить в виде списка. Затем,
с помощью словаря выделите только уникальные (не повторяющиеся) числа.
Сформируйте из них еще один список (уникальных чисел). Числа в этом
списке должны идти в том же порядке, что и при чтении (из входного потока).
Выведите уникальные числа на экран в одну строчку через пробел.

P. S. Такая задача, обычно решается через множества, но мы их еще не проходили,
поэтому воспользуемся словарем.
"""

lst = list(map(int, input().split()))

uniq = list(dict.fromkeys(lst))

print(*uniq)