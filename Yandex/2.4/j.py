n = int(input())

print("А Б В")
a = 1
b = 1
c = n - 2

while True:
    print(f"{a} {b} {c}")
    if c > 1:
        c -= 1
        b += 1
    elif (b != 1) and (c == 1):
        b = 1
        a += 1
        c = n - a - b
    else:
        break
