"""
Анонс новости 2.0

Попробуем ещё раз сократить заголовки для статей в ленте новостного сайта.
Давайте сделаем программу, которая сокращает длинный заголовок до требуемой
длины и завершает его многоточием ..., если это требуется.

Формат ввода
Вводится натуральное число L — необходимая длина заголовка.
Вводится натуральное число N — количество строк в заголовке новости.
В каждой из последующих N строк записано по одной строке заголовка.

Формат вывода
Сокращённый заголовок.

Примечание
Многоточие учитывается при подсчёте длины заголовка.
Символ перевода строки при подсчёте длины не учитывается.
"""

L = int(input())
N = int(input())
text = []

for i in range(N):
    str_text = input()
    if L > 0:
        str_len = len(str_text)
        if L > str_len + 3:
            text.append(str_text)
            L -= str_len
        else:
            text.append(str_text[:(L - 3)] + "...")
            L = 0

for item in text:
    print(item)
