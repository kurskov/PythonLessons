"""Номер купе 🌶️

В купейном вагоне имеется 99 купе с четырьмя местами для пассажиров
в каждом. Напишите программу, которая определяет номер купе,
в котором находится место с заданным номером (нумерация мест сквозная,
начинается с 1).
"""

pos = int(input())

print((pos + 3) // 4)
