# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

sum = int(input('Сколько журавликов сделали ребята: '))
# print("Петя сделал: ", sum//6,"Катя сделала: ", sum//6*4,"Сережа сделал: ", sum//6)

print("Петя сделал:", sum//6)
print("Катя сделала:", sum//6*4)
print("Сережа сделал:", sum//6)