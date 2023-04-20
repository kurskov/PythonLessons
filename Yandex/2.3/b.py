n = 0

while (text := input()) != "Приехали!":
    if "зайка" in text:
        n = n + 1

print(n)
