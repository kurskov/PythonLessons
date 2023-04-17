year = int(input())

if year >= 1582:
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        print("YES")
    else:
        print("NO")
else:
    if (year % 4 == 0):
        print("YES")
    else:
        print("NO")
