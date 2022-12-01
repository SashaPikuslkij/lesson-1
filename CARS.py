class CARS:
    doors = "2-4"
    wheels = "4"
    engine = "all cars"
    def __init__(self, brand, year, colors):
        self.brand = brand
        self.year = year
        self.colors = colors

#цвета
print("1-blue, 2-white, 3-black")

x1 = CARS("Hyndai", 2017, 3)
x2 = CARS("Mercedes", 2015, 1)
x3 = CARS("Kia", 2022, 2)

print(x1.brand)
print(x1.year)
print(x1.colors)

print(x2.brand)
print(x2.year)
print(x2.colors)

print(x3.brand)
print(x3.year)
print(x3.colors)