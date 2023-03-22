# Задача 21: Напишите программу для печати всех уникальных значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
# Примечание: Список словарей задан изначально. Пользователь его не вводит

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
 
my_set = set()
# Вариант 1
# for item in list_1:
#     for value in item.values():
#         my_set.add(value)
# Вариант 2
for item in list_1:
    for key in item.keys():
        my_set.add(item.get(key))
print(my_set)