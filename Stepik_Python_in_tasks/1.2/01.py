age = int(input())
height = float(input())
weight = float(input())

if (age < 10) or (height <= 0) or (height > 3) or (weight <= 0) or (weight > 500):

    print("Ошибочные входные данные")

else:

    bmi = weight / height ** 2  
    bmi = round(bmi, 2)

    if bmi < (18.5 if age < 45 else 22):
        description = "недостаточной массой тела."            
    elif bmi < (25 if age < 45 else 27):
        description = "нормальной массой тела."            
    elif bmi < (30 if age < 45 else 32):
        description = "избыточной массой тела."  
    else:          
        description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)    
