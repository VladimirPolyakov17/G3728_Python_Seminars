# Задача 57: 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data 
# 2. Посмотреть сколько в нем строк и столбцов 
# 3. Определить какой тип данных имеют столбцы
import pandas as pd
# 1. Прочитан
df = pd.read_csv('sample_data/california_housing_test.csv')
df.head() # Просмотр

# 2. 3000 строк и 9 столбцов
df.shape # Кортеж. 3000 строк и 9 столбцов

# 3. Тип данных - float64
df.info() # Информация о типе данных.
df.describe() # Статистика по столбцам #df.describe(include='objecct') - для различных типов данных



# Задача 59: 
# 1. Проверить есть ли в файле пустые значения 
# 2. Показать median_house_value где median_income < 2 
# 3. Показать данные в первых 2 столбцах 
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# 1. Провека есть ли в файле пустые значения 
df.isnull() # обращается к каждому элементу и возвращает значение заполнено или нет, где False – не пустое, и где True – пустое значение.
df.isnull().sum() # статистика по столбцам заполненено или нет.

# 2. Показать median_house_value где median_income < 2
df['median_income'] # Показ столбца
df['median_income'] < 2 # Показ результата по условию в булевой маске
df[df['median_income'] < 2]['median_house_value'] # Показ по условию задачи, где условие ['median_income'] < 2, а выгружаемые данные ['median_house_value'] (может быть много столбцов)

# 3 Показать данные в первых 2 столбцах
df[['longitude', 'latitude']] # 1. Вариант (с перечислением столбцов)
df.columns # Вывод столбцов в виде списка
df.columns[:2] # Срез столбцов
for i in df.columns[:2]: # 2. Вариант
  print(df[i])
df[df.columns[:2]] # 3. Вариант

# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]


# Задача 61: 
# 1. Определить какое максимальное и минимальное значение median_house_value 
# 2. Показать максимальное median_house_value, где median_income = 3.1250 
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value


# 1. Определить какое максимальное и минимальное значение median_house_value 
df['median_house_value'].min(), df['median_house_value'].max() # Вывод данных в виде кортежа

# 2. Показать максимальное median_house_value, где median_income = 3.1250 
df[df['median_income'] == 3.1250] # Вывод таблицы со значением 3.1250
df[df['median_income'] == 3.1250]['median_house_value'] # Вывод значений по условию
df[df['median_income'] == 3.1250]['median_house_value'].max() # Решение

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
df[df['median_house_value'] == df['median_house_value'].min()]['population'].max()
