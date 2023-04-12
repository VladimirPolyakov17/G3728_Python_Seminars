# -*- coding: utf-8 -*-
"""Seminar9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O2-e-sguPGcQVSM2iiyV_MzpRe0PgBEz

# Задача 57:
# 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data 
# 2. Посмотреть сколько в нем строк и столбцов 
# 3. Определить какой тип данных имеют столбцы
"""

import pandas as pd
df = pd.read_csv('sample_data/california_housing_test.csv')
df.head()

df.shape

df.info()

df.info

df.describe() #df.describe(include='objecct') - для различных типов данных

"""# Задача 59: 
# 1. Проверить есть ли в файле пустые значения 
# 2. Показать median_house_value где median_income < 2 
# 3. Показать данные в первых 2 столбцах 
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
"""

df.isnull()

df.isnull().sum()

df['median_income']

df['median_income'] < 2

maska = df['median_income'] < 2
df[maska]

df[df['median_income'] < 2]

df[df['median_income'] < 2]['median_house_value']

df.loc[df['median_income'] < 2]['median_house_value']

"""# 3. Показать данные в первых 2 столбцах """

df[['longitude', 'latitude']]

df.columns

df.columns[:2]

for i in df.columns[:2]:
  print(df[i])

df[df.columns[:2]]

"""# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000"""

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

"""# Задача 61: 
# 1. Определить какое максимальное и минимальное значение median_house_value 
# 2. Показать максимальное median_house_value, где median_income = 3.1250 
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
"""

df['median_house_value'].min(), df['median_house_value'].max()

df[df['median_income'] == 3.1250]

df[df['median_income'] == 3.1250]['median_house_value']

df[df['median_income'] == 3.1250]['median_house_value'].max()

df[df['median_house_value'] == df['median_house_value'].min()]['population'].max()