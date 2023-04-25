n = int(input())
timer = 3

for i in range(1, n + 1):
    for j in range(timer, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i}!!!")
    timer += 1
