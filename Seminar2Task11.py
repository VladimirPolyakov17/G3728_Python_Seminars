# Задача 11: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 
# Output: 6

import os
os.system ('cls')
n= int(input('Введите число: '))
number = 0
number_1 = 1
a = 2
while True:
    sum = number + number_1
    number = number_1
    number_1 = sum
    a +=1
    if sum == n:
        print(a)
        break
    elif sum > n:
        print(-1)
        break