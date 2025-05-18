# Базовий клас
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} видає звук.")

# Дочірній клас Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} каже: Гав!")

    def interact_with_cat(self, cat):
        print(f"{self.name} дивиться на кота {cat.name}.")
        cat.speak()

# Дочірній клас Cat
class Cat(Animal):
    def speak(self):
        print(f"{self.name} каже: Мяу!")

# Створення об'єктів
dog = Dog("Рекс", "Німецька вівчарка")
cat = Cat("Мурчик")

# Перевизначені методи
dog.speak()
cat.speak()

# Взаємодія між об'єктами
dog.interact_with_cat(cat)

# isinstance та issubclass
print("dog є об'єктом Animal:", isinstance(dog, Animal))       # True
print("Cat наслідує Animal:", issubclass(Cat, Animal))         # True
print("cat є об'єктом Dog:", isinstance(cat, Dog))             # False
