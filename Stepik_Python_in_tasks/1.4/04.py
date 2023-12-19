cash = int(input())

if cash < 1 or cash > 99:
    print("ошибка")
elif cash % 10 == 1 and cash != 11:
    print(cash, "рубль")
elif cash % 10 in [2, 3, 4] and cash // 10 != 1:
    print(cash, "рубля")
else:
    print(cash, "рублей")
