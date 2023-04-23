x = int(input())
answer = 0

for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
        answer += 1

if answer != 0 or x == 1:
    print("NO")
else:
    print("YES")
