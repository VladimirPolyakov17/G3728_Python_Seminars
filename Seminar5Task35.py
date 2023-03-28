# Задача 35: Напишите функцию, которая принимает одно число и проверяет, является ли оно простым 
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число) 
# Input: 5 
# Output: yes

# def findSimple(x):
#     for i in range(2,x):
#         if x % i == 0:
#             return "Составное"
#     return "Простое"
# print(findSimple(19))

import math

number = int(input('Введите число: '))
def is_simple(number: int) -> bool:
    if number % 2 == 0:
        return False
    elif number in [1, 2, 3]:
        return True
    else:
        for div in range(3, int(math.sqrt(number) +1, 2)):
            if number % div == 0:
                return False
    return True
print(is_simple(number))