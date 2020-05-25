# 3
# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наименьший элемент столбца матрицы A,
# для которого сумма абсолютных значений элементов максимальна.

import numpy as np
import random

N= random.randint (1,10)
M= random.randint (1,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

mx=0
indmx=0
for i in range (M):
    if np.sum(A[:, i])>mx:
        mx = np.sum(A[:, i])
        indmx=i
print("Столбец с максимальной суммой элементов-"+ str(A[: , indmx]))
print("Сумма этого столбца-"+str(mx)+ ","+ "номер этого столбца-"+ str(indmx+1))
stmin=10
for b in A [: , indmx]:
    if b< stmin:
        stmin=b
print("Минимальный элемент этого столбца-"+str(stmin))
