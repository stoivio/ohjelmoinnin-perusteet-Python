# declare class
class Cat:
    def __init__(self, name="", color=""):
        self.name = name
        self.color = color

    def __miau__(self):
        return "Meoooooow!"


# create instances of Human class
kit = Cat("Kit", "black")
kat = Cat("Kat", "white")

# access class properties
print(kit.name, "Color:", kit.color)
print(kat.name, "Color:", kat.color)

# use class methods
print("Kit says:", kit.__miau__())
print("Kat says:", kat.__miau__())
