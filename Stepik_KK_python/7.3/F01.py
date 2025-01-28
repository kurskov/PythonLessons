"""
Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя
двух натуральных чисел a и b. В программе необходимо объявить функцию get_nod
с двумя параметрами a и b (натуральные числа) и возвращающую значение НОД(a, b).

P. S. Вызывать функцию не нужно, только задать. Постарайтесь реализовать алгоритм,
не возвращаясь к материалу на видео.
"""


def get_nod(a: int, b: int) -> int:
    """Вычисление НОД по быстрому алгоритму Евклида"""
    while b:
        a, b = b, a % b

    return a
