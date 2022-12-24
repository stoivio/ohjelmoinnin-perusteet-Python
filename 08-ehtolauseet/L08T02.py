# find highest value of the numbers
nro1 = int(input("Input integer"))
nro2 = int(input("Input another integer"))
nro3 = int(input("Input one more integer"))

if nro1 > nro2 and nro1 > nro3:
    print("Max value:", nro1)
elif nro2 > nro3:
    print("Max value:", nro2)
else:
    print("Max value:", nro3)

# or make list and find highest value from the list with max()
# print(max([nro1, nro2, nro3]))
