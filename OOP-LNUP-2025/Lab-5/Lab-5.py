# Оголошення класу
class Student:
    def __init__(self, name, age, group):
        self.name = name          # Властивість
        self.age = age            # Властивість
        self.group = group        # Властивість

    # Метод класу
    def introduce(self):
        print(f"Я {self.name}, мені {self.age} років, я з групи {self.group}.")

    def is_adult(self):
        return self.age >= 18

# Створення об’єктів
student1 = Student("Олег", 19, "ІТ-22")
student2 = Student("Марія", 17, "ІТ-22")

# Виклик методів
student1.introduce()
student2.introduce()

# Отримання властивостей
print(f"{student1.name} дорослий? {student1.is_adult()}")
print(f"{student2.name} дорослий? {student2.is_adult()}")

# Зміна властивості
student2.age = 18
print(f"{student2.name} тепер має {student2.age} років.")
print(f"{student2.name} дорослий? {student2.is_adult()}")
