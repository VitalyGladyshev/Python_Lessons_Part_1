# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

print("\nЗадание - 1\n")

import os

name_list = ["Алексй", "Иван", "Пётр", "Николай", "Александр", "Кирилл"]
salary_list = [150000, 250000, 750000, 330000, 700000, 500000]

dir = os.curdir
path = os.path.join(dir, "salary.txt")

with open(path , 'w' , encoding = 'UTF-8') as file_salary:
    for ind_name, ind_salary in dict(zip(name_list, salary_list)).items():
        file_salary.write(f"{ind_name} - {ind_salary}\n")

with open(path , 'r' , encoding = 'UTF-8') as file_salary:
    for line in file_salary:
        val_list = line.split(' ')
        if float(val_list[2]) <= 500000:
            print(f"{val_list[0].upper()} - {float(val_list[2]) * 0.87}")
