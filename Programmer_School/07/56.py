"""
https://acmp.ru/index.asp?main=task&id_task=756
"""

m, n = map(int, input().split())

edges = (m - 1) * n + m * (n - 1)
min_edges = m * n - 1
cuts = edges - min_edges

print(cuts)
