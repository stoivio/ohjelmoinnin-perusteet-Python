def average(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = round(sum / 3, 1)  # round to 1 decimal
    return avg


print(average(2, 4, 6))
