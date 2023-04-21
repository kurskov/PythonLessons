x = 0
y = 0

while (way := input()) != "СТОП":
    steps = int(input())
    match way:
        case "СЕВЕР":
            y += steps
        case "ВОСТОК":
            x += steps
        case "ЮГ":
            y -= steps
        case "ЗАПАД":
            x -= steps

print(y)
print(x)
