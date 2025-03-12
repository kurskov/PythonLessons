"""
На вход программе подается целое неотрицательное число n, которое читается командой:

n = int(input())

Необходимо объявить рекурсивную функцию fact_rec со следующей сигнатурой:

def fact_rec(n): ...

для вычисления факториала числа n. Напомню, что факториал числа, равен:

n!=1⋅2⋅3⋅...⋅nn!=1⋅2⋅3⋅...⋅n

Функция должна возвращать вычисленное значение. Вызывать функцию не нужно, только объявить.
"""

n = int(input())

def fact_rec(n: int) -> int:
    return n * fact_rec(n - 1) if n > 0 else 1
