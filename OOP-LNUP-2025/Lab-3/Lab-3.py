# Умовні оператори
age = int(input("Введіть ваш вік: "))

if age < 18:
    print("Ви неповнолітній.")
elif age >= 18 and age < 60:
    print("Ви дорослий.")
else:
    print("Ви пенсіонер.")

# Булева логіка і складні умови
has_passport = True
has_ticket = False

if has_passport and has_ticket:
    print("Ви можете летіти.")
else:
    print("Потрібні як паспорт, так і квиток.")

# Цикл for
print("Вивід парних чисел від 0 до 10:")
for i in range(11):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Цикл while
print("Зворотній відлік з 5:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Старт!")

# Приклад вкладеної логіки
number = int(input("Введіть число: "))

if number > 0:
    if number % 2 == 0:
        print("Додатне парне число")
    else:
        print("Додатне непарне число")
elif number < 0:
    print("Від’ємне число")
else:
    print("Це нуль")
