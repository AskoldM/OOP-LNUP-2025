class Book:
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.code = f"{author[:3].upper()}-{year}"
        Book.total_books += 1

    # Звичайний метод
    def get_description(self):
        return f"'{self.title}' написана {self.author} у {self.year} (код: {self.code})"

    # Метод класу
    @classmethod
    def get_total_books(cls):
        return f"Всього створено книг: {cls.total_books}"

    # Альтернативний конструктор
    @classmethod
    def from_string(cls, data_str):
        title, author, year = data_str.split(";")
        return cls(title.strip(), author.strip(), int(year.strip()))

    # Статичний метод
    @staticmethod
    def is_classic(year):
        return year < 1950

# Створення об'єкта звичайним способом
book1 = Book("Гаррі Поттер і філософський камінь ", "Дж. К. Ролінґ", 1997)
print(book1.get_description())

# Створення об'єкта альтернативним конструктором
book2 = Book.from_string("Гаррі Поттер і Орден Фенікса; Дж. К. Ролінґ; 2003")
print(book2.get_description())

# Виклик методу класу
print(Book.get_total_books())

# Перевірка статичного методу
print(f"{book1.title} — класика? {Book.is_classic(book1.year)}")
print(f"{book2.title} — класика? {Book.is_classic(book2.year)}")

# Перевірка на сучасну книгу
book3 = Book.from_string("Гаррі Поттер і смертельні реліквії; Дж. К. Ролінґ; 2007")
print(book3.get_description())
print(f"{book3.title} — класика? {Book.is_classic(book3.year)}")
