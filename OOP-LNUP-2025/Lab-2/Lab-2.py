# Змінні та прості типи
x = 10           # int
y = 3.14         # float
name = "Аскольд"    # str
is_student = True  # bool

# Вивід змінних
print(f"Ім'я: {name}, Вік: {x}, Число Пі: {y}, Студент: {is_student}")

# Динамічна типізація
z = "10"
z = int(z) + 5
print("Значення z:", z)

# Операції
a = 5
b = 2
print("a + b =", a + b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)

# Робота зі списком
fruits = ["яблуко", "банан", "вишня"]
print("Другий фрукт:", fruits[1])
fruits.append("груша")
print("Оновлений список:", fruits)

# Умова
if "банан" in fruits:
    print("Банан є в списку!")

# Цикл
for fruit in fruits:
    print("Фрукт:", fruit)

# Форматування рядків
message = "Мене звати {} і мені {} років".format(name, x)
print(message)

# Робота зі стрічками як списками
text = "Програмування"
print("Перші 5 символів:", text[:5])
print("Реверс:", text[::-1])

# Словник
student = {
    "ім'я": "Аскольд",
    "вік": 18,
    "курс": 2
}
print("Ім'я студента:", student["ім'я"])
print("Повний словник:", student)