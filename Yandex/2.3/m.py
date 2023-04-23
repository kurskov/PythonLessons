n = int(input())
win_name = ""

for i in range(n):
    new_name = input()
    if win_name == "":
        win_name = new_name
    else:
        win_name = min(win_name, new_name)

print(win_name)
