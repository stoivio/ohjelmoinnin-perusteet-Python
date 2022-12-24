# Ohjelma, joka näyttää, onko annettu vuosi karkausvuosi.
# Algoritmi:
# 4:llä jaolliset on, paitsi täydet vuosisadat. Kuitenkin 400:lla jaolliset vuosisadat ovat karkausvuosia.
# Esim. 1991 -> ei, 1992 -> on, 1900 -> ei, 2000 -> on

line = int(input("Insert year: "))


def check_leap_year(year):
    # % is modulo operator (jakojäännös)
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return "Is a leap year!"
    else:
        return "Is not leap year!"


print(check_leap_year(line))
