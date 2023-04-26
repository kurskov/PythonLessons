"""
Редизайн таблицы умножения

Согласитесь, что предыдущие таблицы умножения выглядят не очень красиво. 
Давайте зададим для всех столбцов одинаковую ширину, а значения в ячейках выровним по центру.
И да, заказчик попросил ещё добавить в таблицу рамки между ячейками.

Формат ввода
В первой строке записан требуемый размер таблицы. 
Во второй строке — ширина столбцов.

Формат вывода
Таблица умножения заданного размера и вида.

Примечание
Ответ на первый тест должен выглядеть так:

 1 | 2 | 3 
-----------
 2 | 4 | 6 
-----------
 3 | 6 | 9 
"""

n = int(input())
width = int(input())

for i in range(1, n + 1):
    row = ""
    for j in range(1, n + 1):
        text = str(i * j)
        k = 1
        while len(text) < width:
            if k % 2 != 0:
                text += " "
            else:
                text = " " + text
            k += 1
        row += text
        if j < n:
            row += "|"
    print(row)
    if i < n:
        print("-" * (width * n + (n - 1)))