"""
https://acmp.ru/index.asp?main=task&id_task=685
"""

lst = list(map(int, input().split()))

prices = iter(sorted(lst[:3]))
boxes = iter(sorted(lst[3:]))
result = 0
for _ in range(3):
    result += next(prices) * next(boxes)

print(result)
