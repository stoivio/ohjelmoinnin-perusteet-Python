line = 0
sum = 0
i = 0
while True:
    line = input("Anna luku: ")
    if line == "":
        break
    sum += int(line)
    i += 1

print("Lukuja annettu:", i)
print("Lukujen summa:", sum)
