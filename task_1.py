#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Импортировал библиотеки: pandas — для обработки данных, matplotlib — для визуализации
import pandas as pd
import matplotlib.pyplot as plt

# Убрал строки, в которых есть хотя бы одно пропущенное значение 
flights = pd.read_csv('flights_NY.csv').dropna(axis=0)

# Высчитал вероятность положительной задержки прилёта
prob_delays = flights.groupby('carrier')['arr_delay'].apply(lambda x: (x > 0).mean())

# Для визуализации выбрал наиболее очевидный вариант — гистограмму
plt.figure(figsize=(9, 6))
prob_delays.plot(kind='bar', color="#bd2a83")
plt.xlabel('Авиакомпания')
plt.ylabel('Вероятность положительной задержки прилёта')
plt.title('Распределение вероятности положительной задержки по авиакомпаниям', fontsize=12)
plt.show()

