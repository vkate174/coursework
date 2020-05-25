# 16
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Исключить из матрицы строку с номером L.
# Сомкнуть строки матрицы.

import numpy as np

N = 4
M = 5

L = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix = np.delete(matrix, L, axis=0)
print("Полученная матрица:\r\n {}".format(matrix))
