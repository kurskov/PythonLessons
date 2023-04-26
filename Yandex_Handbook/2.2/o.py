n = sorted(input() + input())

middle = (int(n[1]) + int(n[2])) % 10

print(f"{n[3]}{middle}{n[0]}")
