# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a n = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5 
# Вывод: 7 9 11 13 15

a1 = int(input("Введите значение а1: "))
d = int(input("Введите значение d (шаг): "))
n = int(input("Введите значение n(количество чисел массива): "))
an = [a1 + (i-1)*d for i in range(1, n +1)]
print(an)

