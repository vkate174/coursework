# 9
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить, сколько нулевых элементов
# содержится в верхних L строках матрицы и в левых К столбцах матрицы.


import numpy as np

N = np.random.randint(2,10)
M = np.random.randint(2,10)
L = np.random.randint(1,N)
K = np.random.randint(1,M)

print(N,M,L,K)
A=np.random.randint(-10,10, (N,M))

New_A = A[:L, :K]

print(A)

print(np.sum(New_A == 0))
