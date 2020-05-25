# 14
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы матрицы на элемент матрицы
# с наибольшим значением.

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

max_el = np.max(matrix)
matrix = matrix / max_el
print("Полученная матрица:\r\n {}".format(matrix))
