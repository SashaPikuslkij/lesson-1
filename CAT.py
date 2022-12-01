class CAT:
    paws = "4"
    sound = "мяу"
    skincovering = "шерсть"
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        #print(id(self))


x1 = CAT("Барсик", 3, 10)
x2 = CAT("Вася", 6, 13)
x3 = CAT("Просто кот", 2, 8)

print(x1.name)
print(x2.name)
print(x3.name)

print(x1.age)
print(x2.age)
print(x3.age)

print(x1.weight)
print(x2.weight)
print(x3.weight)

