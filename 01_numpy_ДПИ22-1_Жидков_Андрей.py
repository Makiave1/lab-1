#!/usr/bin/env python
# coding: utf-8

# # Numpy

# Материалы:
# * Макрушин С.В. "Лекция 1: Библиотека Numpy"
# * https://numpy.org/doc/stable/user/index.html
# * https://numpy.org/doc/stable/reference/index.html

# ## Задачи для совместного разбора

# 1. Сгенерировать двухмерный массив `arr` размерности (4, 7), состоящий из случайных действительных чисел, равномерно распределенных в диапазоне от 0 до 20. Нормализовать значения массива с помощью преобразования вида  $𝑎𝑥+𝑏$  так, что после нормализации максимальный элемент масcива будет равен 1.0, минимальный 0.0

# In[4]:


import numpy as np


# In[7]:


a = np.random.uniform(0, 20, size = (4, 7))
(a - a.min() )/ ((a.max() - a.min()))


# 2. Создать матрицу 8 на 10 из случайных целых (используя модуль `numpy.random`) чисел из диапозона от 0 до 10 и найти в ней строку (ее индекс и вывести саму строку), в которой сумма значений минимальна.

# In[4]:


import numpy as np
a = np.random.uniform(0, 10, size = (8, 10))
print(a)
b = np.sum(a, axis=1)
print(b)
np.argmin(b)


# 3. Найти евклидово расстояние между двумя одномерными векторами одинаковой размерности.

# In[10]:


import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D


# In[ ]:





# 4. Решить матричное уравнение `A*X*B=-C` - найти матрицу `X`. Где `A = [[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]]`, `B=[[3, -1], [2, 1]]`, `C=[[7, 21], [11, 8], [8, 4]]`.

# ## Лабораторная работа №1

# Замечание: при решении данных задач не подразумевается использования циклов или генераторов Python, если в задании не сказано обратного. Решение должно опираться на использования функционала библиотеки `numpy`.

# 1. Файл `minutes_n_ingredients.csv` содержит информацию об идентификаторе рецепта, времени его выполнения в минутах и количестве необходимых ингредиентов. Считайте данные из этого файла в виде массива `numpy` типа `int32`, используя `np.loadtxt`. Выведите на экран первые 5 строк массива.

# In[9]:


import numpy as np
a = np.loadtxt('minutes_n_ingredients.csv', dtype=np.int32, delimiter=',', skiprows=1, max_rows=5)
print(a_ld)


# 2. Вычислите среднее значение, минимум, максимум и медиану по каждому из столбцов, кроме первого.

# In[ ]:


print('Среднее по 2му столбцу: ', np.around(np.mean(a[:,1])))
print('Среднее по 3му столбцу: ', np.around(np.mean(a[:,2])))
print('Минимум по 2му столбцу: ', np.amin(a[:,1]))
print('Минимум по 3му столбцу: ', np.amin(a[:,2]))
print('Максимум по 2му столбцу: ', np.amax(a[:,1]))
print('Максимум по 3му столбцу: ', np.amax(a[:,2]))
print('Медиана по 2му столбцу: ', np.median(a[:,1]))
print('Медиана по 3му столбцу: ', np.median(a[:,2]))


# 3. Ограничьте сверху значения продолжительности выполнения рецепта значением квантиля $q_{0.75}$. 

# In[ ]:


q = np.quantile(a[:,1], q = 0.75)
a[:,1] = a[:,1].clip(max = q)


# 4. Посчитайте, для скольких рецептов указана продолжительность, равная нулю. Замените для таких строк значение в данном столбце на 1.

# In[11]:


zeros = len(a[:,1])-np.count_nonzero(a[:,1]) 
print(zeros)
np.place(a[:,1], a[:,1] == 0, 1)


# 5. Посчитайте, сколько уникальных рецептов находится в датасете.

# In[10]:


len(np.unique(a, axis = 0))


# 6. Сколько и каких различных значений кол-ва ингредиентов присутвует в рецептах из датасета?

# In[12]:


print(len(np.unique(a[:,2])))
print(np.unique(a[:,2]))


# 7. Создайте версию массива, содержащую информацию только о рецептах, состоящих не более чем из 5 ингредиентов.

# In[ ]:


i5 = a[(a[:,2] < 5) | (a[:,2] == 5)]
len(i5)


# 8. Для каждого рецепта посчитайте, сколько в среднем ингредиентов приходится на одну минуту рецепта. Найдите максимальное значение этой величины для всего датасета

# In[ ]:


m = np.divide(a[:,2], a[:,1])
np.amax(m)


# 9. Вычислите среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью

# In[ ]:


arrCopy = a[a[:, 1].argsort()[::-1]] 
srIn = aCopy[0:100,:] # Топ-100
print(np.mean(srIn[:,2]))


# 10. Выберите случайным образом и выведите информацию о 10 различных рецептах

# In[ ]:


idx = np.random.randint(100000, size=10)
rows = a[idx, :]
print(rows)


# 11. Выведите процент рецептов, кол-во ингредиентов в которых меньше среднего.

# In[ ]:


k = len(a[(a[:,2] < (np.mean(a[:,2])))])
k1 = k / len(a) * 100
print(k1, '%', sep = '')


# 12. Назовем "простым" такой рецепт, длительность выполнения которого не больше 20 минут и кол-во ингредиентов в котором не больше 5. Создайте версию датасета с дополнительным столбцом, значениями которого являются 1, если рецепт простой, и 0 в противном случае.

# In[ ]:


s = np.zeros((100000, 1), dtype = np.int32)
a = np.append(a, s, 1)
np.place(a[:,3], (((a[:,1] < 20) | (a[:,1] == 20)) & ((a[:,2] < 5) | (a[:,2] == 5))), 1)
a


# 13. Выведите процент "простых" рецептов в датасете

# In[ ]:


p = len(a[(a[:,3] == 1)])
p1 = p / len(a) * 100
print(p1, '%', sep = '')


# 14. Разделим рецепты на группы по следующему правилу. Назовем рецепты короткими, если их продолжительность составляет менее 10 минут; стандартными, если их продолжительность составляет более 10, но менее 20 минут; и длинными, если их продолжительность составляет не менее 20 минут. Создайте трехмерный массив, где нулевая ось отвечает за номер группы (короткий, стандартный или длинный рецепт), первая ось - за сам рецепт и вторая ось - за характеристики рецепта. Выберите максимальное количество рецептов из каждой группы таким образом, чтобы было возможно сформировать трехмерный массив. Выведите форму полученного массива.

# In[ ]:




