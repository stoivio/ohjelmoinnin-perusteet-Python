def kerro3():
    age = int(input("How old are you?"))
    if age < 13:
        return "child"
    elif age >= 13 and age <= 19:
        return "teen"
    elif age >= 20 and age <= 65:
        return "adult"
    else:
        return "senior"


age = kerro3()
print(age)
