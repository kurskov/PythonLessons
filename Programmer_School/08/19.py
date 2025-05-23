"""
https://acmp.ru/index.asp?main=task&id_task=819
"""

a, b, c = map(int, input().split())

S = 2 * (a * b + b * c + a * c)
V = a * b * c

print(S, V)
