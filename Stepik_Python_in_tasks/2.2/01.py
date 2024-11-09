import math


def compute_population(t):
    
    population = (172 / 45) * (math.pi / 2 - math.atan((2000 - t) / 45))
    
    return population


time_start= int(input("Введите начало диапазона поиска: "))
time_stop = int(input("Введите конец диапазона поиска: "))

for x in range(time_start, time_stop + 1):
    if compute_population(x) > 9:
        print(x)
        break
