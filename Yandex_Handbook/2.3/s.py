L = 1
R = 1001

m = (R + L) // 2
print(m)

while (R - L > 1) and ((text := input()) != "Угадал!"):
    if text == "Меньше":
        R = m
    elif text == "Больше":
        L = m
    m = (R + L) // 2
    print(m)
