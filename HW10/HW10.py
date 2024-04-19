import pandas as pd

# Создаем исходный DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем таблицу с одним столбцом
table = pd.pivot_table(data.assign(count=1), index=data.index, columns='whoAmI', values='count', fill_value=0)
pd.options.display.float_format = "{:.0f}".format

# Выводим результат в командную строку
print(table)