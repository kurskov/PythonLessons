pet = float(input())
vas = float(input())
tol = float(input())

if pet == max(pet, vas, tol):
    print("1. Петя")
    if vas > tol:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася")
elif vas == max(pet, vas, tol):
    print("1. Вася")
    if pet > tol:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
else:
    print("1. Толя")
    if pet > vas:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")
