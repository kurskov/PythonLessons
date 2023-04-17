pet = float(input())
vas = float(input())
tol = float(input())

if pet == max(pet, vas, tol):
    print("Петя")
elif vas == max(pet, vas, tol):
    print("Вася")
else:
    print("Толя")
