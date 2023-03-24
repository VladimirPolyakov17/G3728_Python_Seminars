# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X
# Например:
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите размер массива: "))
mass = str(input("Вводите числа в массиве: ")).split()
search = int(input("Введите искомое число X: "))

mass = [int(i) for i in mass]

answer = set()
answer.add(mass[0])
total = abs(mass[0]-search)

for i in mass:
    if abs(i-search) < total:
        total = abs (i-search)
        answer.clear()
        answer.add(i)
    elif abs(i-search) == total:
        answer.add(i)
print(f'Элементы, ближайшие по величине к заданому числу: {answer}')