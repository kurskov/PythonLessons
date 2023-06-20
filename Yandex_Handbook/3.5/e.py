"""А роза упала на лапу Азора 6.0

Мы уже писали программы, которые определяли, а палиндром перед нами или нет.
Давайте теперь найдём все слова-палиндромы среди введённых строк.

Формат ввода
Вводятся слова.

Формат вывода
Список слов-палиндромов в алфавитном порядке без повторений.

Примечание
При проверке слов не обращайте внимание на регистр.
"""

from sys import stdin

words = set()
for line in stdin:
    wodrs_in_line = set(line.rstrip("\n").split())
    words |= wodrs_in_line

for word in sorted(words):
    flip_word = list(word.lower())
    flip_word.reverse()
    if "".join(flip_word) == word.lower():
        print(word)
