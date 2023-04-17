v1 = int(input())
v2 = int(input())
v3 = int(input())

if (v1 % 10) == (v2 % 10) == (v3 % 10):
    print(v1 % 10)

if (v1 // 10 % 10) == (v2 // 10 % 10) == (v3 // 10 % 10):
    print(v1 // 10 % 10)
