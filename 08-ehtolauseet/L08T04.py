points = int(input("Give amount of points: "))
grade = 0

if points in range(0, 1):
    grade = 0
elif points in range(2, 3):
    grade = 1
elif points in range(4, 5):
    grade = 2
elif points in range(6, 7):
    grade = 3
elif points in range(8, 9):
    grade = 4
elif points in range(10, 12):
    grade = 5
else:
    print("Invalid amount of points")

print("Grade is:", grade)
