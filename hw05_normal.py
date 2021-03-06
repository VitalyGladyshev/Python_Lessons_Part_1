# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое (not текущей) папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_easy

print("Задача-1\n")

print("1. Перейти в папку\n"
        "2. Просмотреть список папок\n"
        "3. Удалить папку\n"
        "4. Создать папку\n")
command_str = input("Введите номер команды (1-4): ")
if command_str == '1':
    ch_dir = input("Введите папку назначения: ")
    if os.path.exists(ch_dir):
        os.chdir(ch_dir)
        print(os.listdir(ch_dir))
    else:
        print(f"Папка {ch_dir} не существует")
elif command_str == '2':
    list_dir = input("Введите папку для просиотра содержимого: ")
    res_list_dir = hw05_easy.list_dir(list_dir)
    if res_list_dir != False:
        print(res_list_dir)
    else:
        print("Данная папка не существует!")
elif command_str == '3':
    del_dir = input("Введите имя удаляемой папки: ")
    res_del_dir = hw05_easy.dir_delete(del_dir)
    if res_del_dir:
        print(f"Ошибка: {res_del_dir}")
elif command_str == '4':
    cr_dir = input("Введите имя новой папки: ")
    if hw05_easy.dir_create(cr_dir):
        print(f"Папка {cr_dir} уже существует")
else:
    print("Команда не распознана")
