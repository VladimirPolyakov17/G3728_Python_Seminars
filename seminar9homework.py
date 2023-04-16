# -*- coding: utf-8 -*-
"""Seminar9HomeWork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FjE8Uu1rqxld1RRHS0lUx4s8IHxJjFUk
"""

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

df.head()

"""# Задача 40: Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)S

"""

df[df['population'] < 500]['median_house_value'].mean()

"""# Задача 42: Узнать какая максимальная households в зоне минимального значения population"""

df[df['population'] == df['population'].min()]['households'].max()