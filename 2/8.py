# 8
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить, сколько отрицательных элементов
# содержится в каждом столбце и в каждой строке матрицы. Результат
# оформить в виде матрицы из N + 1 строк и M + 1 столбцов.

import numpy as np
import random
N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)
A=np.random.randint(-10,10, (N,M))

print(A)
M_sum = (A < 0).sum(axis=0)
N_sum = (A < 0).sum(axis=1)

print("Кол-во отрицательных элементов в матрице-"+str(M_sum ), str(N_sum))

N_sum = np.append(N_sum, None)

A = np.vstack((A, M_sum))
A = np.hstack((A, N_sum.reshape(-1,1)))

print("Матрица с N и M +1-",A)
