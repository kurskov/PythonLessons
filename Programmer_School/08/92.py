"""
https://acmp.ru/index.asp?main=task&id_task=892
"""

n = int(input())

if n in [1, 2, 12]:
    print('Winter')
elif n in [2, 4, 5]:
    print('Spring')
elif n in [6, 7, 8]:
    print('Summer')
elif n in [9, 10, 11]:
    print('Autumn')
else:
    print('Error')
