name = str(input())
box = int(input())
pn = box % 10
bed = box // 10 % 10
group = box // 100 % 10
print(f"Группа №{group}.")
print(f"{pn}. {name}.")
print(f"Шкафчик: {box}.")
print(f"Кроватка: {bed}.")
