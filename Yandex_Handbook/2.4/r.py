"""
Новогоднее настроение 2.0

Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
Помогите им, написав программу, которая по введённому числу строит математическую ёлку.

Формат ввода
Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода
Требуемая новогодня ёлка.

Примечание
Не забывайте про существование f-строк.
Ответ на первый тест должен выглядеть так:

     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
"""

n = int(input())
max_line_len = 0

number = 1
for i in range(1, n + 1):
    line_len = -1
    for j in range(1, i + 1):
        line_len += len(str(number)) + 1
        number += 1
        if number > n:
            break
    if max_line_len < line_len:
        max_line_len = line_len
    if number > n:
        break

number = 1
for i in range(1, n + 1):
    text = ""
    for j in range(1, i + 1):
        if j > 1:
            text += " "
        text += str(number)
        number += 1
        if number > n:
            break
    k = 1
    while len(text) < max_line_len:
        if k % 2 != 0:
            text += " "
        else:
            text = " " + text
        k += 1
    print(text)
    if number > n:
        break
