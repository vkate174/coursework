# 6
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждого
# столбца. Результат оформить в виде матрицы из N + 1 строк и M столбцов.

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

B=np.sum(A)
print ("Сумаа элементов матрицы A-", B)

M_sum = np.sum(A, axis=0)/np.sum(A)
print("Доля элементов каждого столбца-"+str(np.sum(A, axis=0)/np.sum(A)))

A = np.vstack((A,M_sum))

print("Матрица с N +1-",A)
