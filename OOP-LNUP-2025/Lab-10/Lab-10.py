class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Приватна змінна

    @property
    def age(self):
        print("Отримання віку")
        return self._age

    @age.setter
    def age(self, value):
        print("Встановлення віку")
        if value < 0:
            raise ValueError("Вік не може бути від’ємним")
        self._age = value

    @age.deleter
    def age(self):
        print("Видалення віку")
        del self._age

# Створення об'єкта
person = Person("Олег", 25)

# Використання @property
print("Вік:", person.age)

# Використання @setter
person.age = 30
print("Оновлений вік:", person.age)

# Видалення віку
del person.age

# Повторна спроба доступу
try:
    print(person.age)
except AttributeError as e:
    print("Помилка:", e)
