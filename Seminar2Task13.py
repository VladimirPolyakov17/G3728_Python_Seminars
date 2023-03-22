# Задача 13: Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 
# Output: 2

# Вариант 1
# import random
# days = int(input('Введите количество дней: '))

# today = 0
# warm_days = 0
# warm_period = 0
# for _ in range(days):
#     print(today, end=' ')
#     today += random.randint(-5, 5)
#     if today > 0:
#         warm_days += 1
#         if warm_period < warm_days:
#             warm_period = warm_days
#     if today < 0:
#         warm_days = 0
# print ("Самая долгая оттепель равно: ", warm_period)
# Вариант 2
import random
days = int(input('Введите количество дней: '))

today = 0

warm_count = 0
max_warm = 0

for _ in range(days):
    today += random.randint(-5, 5)
    print(today, end=' ')
    if today > 0:
        warm_count += 1
    else:
        if max_warm < warm_count:
            max_warm = warm_count
        warm_count = 0
else:
    if max_warm < warm_count:
        max_warm = warm_count
    warm_count = 0
print(f'\nСамая долгая оттепель была {max_warm} дней')