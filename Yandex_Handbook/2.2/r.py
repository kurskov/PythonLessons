a = int(input())
b = int(input())
c = int(input())

x = sorted([a, b, c])

sqr_max = x[2] ** 2
sqr_other = x[1] ** 2 + x[0] ** 2

if sqr_max < sqr_other:
    print("крайне мала")
elif sqr_max > sqr_other:
    print("велика")
else:
    print("100%")
