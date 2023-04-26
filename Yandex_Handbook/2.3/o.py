n = int(input())
count = 0

for i in range(n):
    text = input()
    if "зайка" in text:
        count += 1

print(count)
