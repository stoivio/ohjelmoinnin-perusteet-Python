sum = 0

for i in range(0, 5):
    num = int(input("Input number: "))
    if num > 0:
        sum += num
    else:
        continue

print("Sum is", sum)
