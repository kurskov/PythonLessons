"""
https://acmp.ru/index.asp?main=task&id_task=757
"""

C, H, O = map(int, input().split())

print(min(C // 2, H // 6, O))
