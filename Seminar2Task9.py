# Задание 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while 
# Input: 5 
# Output: 120

number = abs(int(input('Введите число: '))) #abs - модуль, при котором если введешь минусовое число, то будет вывод положительного.

factorial = 1

while number > 1: 
    factorial *= number
    number -= 1
print(factorial)