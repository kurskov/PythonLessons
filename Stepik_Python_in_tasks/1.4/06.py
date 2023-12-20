h, m, s = int(input()), int(input()), int(input())  # h:m:s

if (0 <= h <= 11) and (0 <= m <= 59) and (0 <= s <= 59):

    seconds = s + m * 60 + h * 3600
    angle = 360 * seconds / 43200

    print(round(angle, 2))

else:

    print("error")
