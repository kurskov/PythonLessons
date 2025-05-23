"""
https://acmp.ru/index.asp?main=task&id_task=66
"""

keys = 'qwertyuiopasdfghjklzxcvbnm'

sym = input()
next_sym_id = (keys.index(sym) + 1) % 26

print(keys[next_sym_id])
