# declare class
class Human:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        print("Name is", self.name, "and age is", self.age)


# create instances of Human class
adam = Human("Adam", 18)
eve = Human("Eve", 18)

# use class methods
adam.__str__()
eve.__str__()
