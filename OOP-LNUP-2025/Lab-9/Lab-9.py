import math

# Базовий клас
class Shape:
    def area(self):
        pass

# Клас кола
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Коло з радіусом {self.radius}"

# Клас прямокутника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямокутник {self.width}x{self.height}"

    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.area() == other.area()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented

# Демонстрація поліморфізму
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]

for shape in shapes:
    print(str(shape))
    print("Площа:", shape.area())

# Магічні методи
rect1 = Rectangle(2, 3)
rect2 = Rectangle(4, 1.5)
print("\nrect1 == rect2:", rect1 == rect2)
rect3 = rect1 + rect2
print("Новий прямокутник після додавання:", rect3)
print("Площа нового прямокутника:", rect3.area())
