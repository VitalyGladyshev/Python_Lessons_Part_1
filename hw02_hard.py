# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

print("Задание-1")
member_list = equation.split(' ')
par = float(member_list[2][:len(member_list[2]) - 1])
displ = float(member_list[len(member_list) - 1])
if member_list[3] == '-':
    displ *= -1
print(f"Координата y прямой вида y = kx + b: {par * x + displ}\n")

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

print("Задание-2")

month_len_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
if len(date) != 10 or date.count('.') != 2:
    print("Дата не соответствует формату dd.mm.yyyy!")
else:
    member_list = date.split('.')
    if not (len(member_list[0]) == 2 and member_list[0].isdecimal() and 1 <= int(member_list[0]) <= 31):
        print("Некорректно задан день!")
    elif not (len(member_list[1]) == 2 and member_list[1].isdecimal() and 1 <= int(member_list[1]) <= 12):
        print("Некорректно задан месяц!")
    elif not (len(member_list[2]) == 4 and member_list[2].isdecimal() and 1 < int(member_list[2])):
        print("Некорректно задан год!")
    elif month_len_tuple[int(member_list[1]) - 1] < int(member_list[0]):
        print("День не соответствует длине месяца!")
    else:
        print(f"Дата соответствует формату. День: {member_list[0]} месяц: {member_list[1]} год: {member_list[2]}")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3