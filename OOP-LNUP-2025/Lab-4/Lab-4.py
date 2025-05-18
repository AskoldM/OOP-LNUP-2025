# Проста функція
def greet(name):
    print(f"Привіт, {name}!")

greet("Оля")

# Функція з параметрами та поверненням значення
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print("Результат множення:", result)

# Іменовані аргументи
def describe_person(name, age, city="Львів"):
    print(f"{name} має {age} років і живе в місті {city}")

describe_person("Іван", 22)
describe_person(age=19, name="Марія", city="Київ")

# Callback-функція
def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Сума:", apply_operation(10, 5, add))
print("Різниця:", apply_operation(10, 5, subtract))

# Вкладена функція
def outer_function(message):
    def inner_function():
        print("Повідомлення:", message)
    inner_function()

outer_function("Це вкладена функція")
