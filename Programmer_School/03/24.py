"""
https://acmp.ru/index.asp?main=task&id_task=324
"""

s = input()
print("YES" if s[:2] == s[:1:-1] else "NO")
