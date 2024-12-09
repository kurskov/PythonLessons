"""
На вход программе подается натуральное число n. Прочитайте это число и
с помощью цикла for определите является ли оно простым (то есть, делится
нацело только на само себя и на 1). Вывести на экран строку "ДА", если
n простое и строку "НЕТ" в противном случае.
"""

n = int(input())

for i in range(2, int(n ** 0.5) + 1):
    if not n % i:
        print("НЕТ")
        break
else:
    print("ДА")