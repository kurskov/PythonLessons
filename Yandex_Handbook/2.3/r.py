n = int(input())
answer = ""

for i in range(2, n + 1):
    while n % i == 0:
        if answer != "":
            answer += " * " + str(i)
        else:
            answer = str(i)
        n /= i

print(answer)
