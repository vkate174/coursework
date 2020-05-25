# 17
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к матрице строку и вставить ее под
# номером L.


import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)
L = 1
print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

row = np.random.randint(low=-9, high=10, size=M)
print("Строка для вставки: {}".format(row))

matrix = np.insert(matrix, L, row, axis=0)
print("Полученная матрица:\r\n {}".format(matrix))
