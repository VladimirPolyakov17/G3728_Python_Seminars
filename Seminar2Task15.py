# Задача 15: Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! 
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 
# Output: 1 9 

# Вариант 1
# from random import randint
# watermelon = int (input('Введите количество арбузов: '))
# max_watermelon = 1000
# min_watermelon = 30000
# while watermelon !=0:
#     weight = randint(1000, 30000)
#     print(weight, end=' ')
#     if weight > max_watermelon:
#         max_watermelon = weight
#     if weight < min_watermelon:
#         min_watermelon = weight
#     watermelon -=1
# print()
# print(f'Самый тяжелый арбуз {max_watermelon} кг')
# print(f'Самый легкий арбуз {min_watermelon} кг')

# Вариант 2
from random import randint
count = int(input('Введите количтсво арбузов: '))

min_weight = 30000
max_weight = 1000
for _ in range(count):
    current_weight = randint(1000, 30000)
    print (current_weight, end=' ')
    if min_weight > current_weight:
        min_weight = current_weight
    if max_weight < current_weight:
        max_weight = current_weight
print(f'\nВзял для себя арбуз весом {max_weight} кг, a теще {min_weight} кг')