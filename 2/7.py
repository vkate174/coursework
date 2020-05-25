# 7
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждой
# строки. Результат оформить в виде матрицы из N строк и M+1 столбцов.

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

B=np.sum(A)
print ("Сумаа элементов матрицы A-", B)

N_sum = np.sum(A, axis=1)/np.sum(A)
print("Доля элементов каждой строки-"+str(np.sum(A, axis=1)/np.sum(A)))

A = np.hstack((A, N_sum.reshape(-1,1)))

print("Матрица с M +1-",A)
