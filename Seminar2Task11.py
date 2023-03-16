# Задача 11: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 
# Output: 6

# Вариант 1
# import os
# os.system ('cls')
# n= int(input('Введите число: '))
# number = 0
# number_1 = 1
# a = 2
# while True:
#     sum = number + number_1
#     number = number_1
#     number_1 = sum
#     a +=1
#     if sum == n:
#         print(a)
#         break
#     elif sum > n:
#         print(-1)
#         break

# Вариант 2
# x = int(input("Введите искомое число Фибоначчи: "))
# fib_prev = 0
# fib_curr = 1
# n = 1

# while fib_curr < x:
#     fib_next = fib_prev + fib_curr
#     fib_prev = fib_curr
#     fib_curr = fib_next
#     n += 1

# if fib_curr == x:
#     print(n)
# else: 
#     print(-1)

# Вариант 3
number = int (input('Введите число: '))

fibo_1, fibo_2, index = 0, 1, 1

while fibo_2 < number:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    index += 1

if fibo_2 == number:
    print(index)
else:
    print(-1)
