# 22
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Исходная матрица состоит из нулей и единиц.
# Добавить к матрице еще один столбец, каждый элемент которого делает
# количество единиц в каждой строке чётным.


import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)

A = np.random.randint(low=0, high=2, size=(N, M))
print("Матрица:\r\n{}".format(A))

col = [i % 2 for i in np.sum(A, axis=1)]

A = np.insert(A, M, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))
