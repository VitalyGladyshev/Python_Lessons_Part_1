# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

var = input("Введите имя: ")
print("Вы ввели: ", var)
print(type(var))
var = int(input("Введите возраст: "))
print("Вы ввели: ", var)
print(type(var))
var = float(input("Введите число Пи: "))
print("Вы ввели: ", var)
print(type(var))

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

var = int(input("Введите целое число: "))
print(var, "+ 2 = ", var + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите ваш возраст (число целых лет): "))
while not 0 < age <= 119:
    age = int(input("Введите ваш возраст (число целых лет): "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
