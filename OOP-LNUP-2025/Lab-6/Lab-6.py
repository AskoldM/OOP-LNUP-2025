class Book:
    # Змінна класу (спільна для всіх об'єктів)
    total_books = 0

    def __init__(self, title, author, year):
        # Змінні об’єкта
        self.title = title
        self.author = author
        self.year = year
        self.code = f"{author[:3].upper()}-{year}"

        # Збільшуємо лічильник створених об'єктів
        Book.total_books += 1

    # Метод об’єкта
    def get_description(self):
        return f"'{self.title}' написана {self.author} у {self.year} (код: {self.code})"

    # Метод класу
    @classmethod
    def get_total_books(cls):
        return f"Всього створено книг: {cls.total_books}"

# Створення об’єктів
book1 = Book("Місто", "Валер'ян Підмогильний", 1927)
book2 = Book("Тигролови", "Іван Багряний", 1944)

# Виклики методів
print(book1.get_description())
print(book2.get_description())

# Виклики методів класу
print(Book.get_total_books())
