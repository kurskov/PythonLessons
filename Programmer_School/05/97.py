"""
https://acmp.ru/index.asp?main=task&id_task=597
"""

r1, r2, r3 = map(int, input().split())
print("YES" if r1 >= r2 + r3 else "NO")
