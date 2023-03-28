# Задача 37: Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 
# Output: 4 3

# Задача: угадай число

number = int(input("Введите число: "))

max_limit = 1000
min_limit = 0
hidden = (max_limit + min_limit)//2

while hidden != number:
    print(f'Я думаю, что это {hidden}')
    choice = input('Больше (>) или меньше (<): ')
    if choice == '<':
        max_limit = hidden
    else:
        min_limit = hidden
    hidden = (max_limit + min_limit) // 2
print(f'Ты загадал {hidden}')