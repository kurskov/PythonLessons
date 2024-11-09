import math


def compute_population(t):
    
    population = (172 / 45) * (math.pi / 2 - math.atan((2000 - t) / 45))
    
    return population


years_str_list = input().split()

years_list = [int(x) for x in years_str_list]

n = len(years_list)

for i in range(n):
    print(f"{years_list[i]:5d} - "
          f"{compute_population(years_list[i]):6.3f} миллиард(ов)")   
