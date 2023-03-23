# Задача 25: Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Вариант 1
# my_string='a a a b c a a d c d d'
# print(my_string)
# my_string=list(my_string.split())
# print(my_string)
# temp=[]
# for i in my_string:
#     if i in temp:
#         print(f'{i}_{temp.count(i)}', end=' ')
#         temp.append(i)
#     else:
#         print(i, end=' ')
#         temp.append(i)

# Вариант 2
import random
import string # Коллекция

# print(string.ascii_letters) # Буквы маленькие и больше английские
# print(string.digits) # Цифры
# print(string.ascii_lowercase+string.digits) # Сбор коллекции

all_chars =string.ascii_lowercase + string.digits

my_string = [random.choice(all_chars) for _ in range(20)] # Случайный выбор из коллекции 20 штук
print(my_string)
dict_count = {} # Пустой словарь

for item in my_string: # Перебор полученных данных
    dict_count[item] = dict_count.get(item, -1) + 1 # Создаем ключ с присваиванием, при повторении увеличиваем на 1
    if dict_count.get(item) > 0:
        print(f'{item}_{dict_count.get(item)}' , end=' ') # Вывод значения и кол-во на печать
    else:
        print(item, end=' ')
