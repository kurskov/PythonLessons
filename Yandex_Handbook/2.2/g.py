val = int(input())

v0 = val % 10
v1 = val // 10 % 10
v2 = val // 100 % 10
v3 = val // 1000 % 10

if (str(v3) + str(v2)) == (str(v0) + str(v1)):
    print("YES")
else:
    print("NO")
