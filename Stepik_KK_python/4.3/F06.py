"""
Объявите в программе следующий список названий нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Затем, на вход программе подаются три целых числа в диапазоне от 1 до 7
в одну строчку через пробел: номера нот. Необходимо прочитать эти числа
и сформировать строку с названиями прочитанных номеров нот, следующих
в строчку через пробел. Дополнительно перед нотами до и фа поставить
символ диеза '#'.

Реализовать программу с использованием тернарного условного оператора
(он может применяться несколько раз).
"""

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

nums = list(map(int, input().split()))

names = [("#" if i in [1, 4] else "") + m[i - 1] for i in nums]

print(*names)
