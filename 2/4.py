#4
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наименьшее значение среди средних
# значений для каждой строки матрицы.

import numpy as np
import random

N= random.randint (1,10)
M= random.randint (1,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

mx=10
aver=0
for i in range (N):
    if np.mean (A[i , :])< mx:
        mx= np.mean(A[i , :])
        aver=i
print("Строка с минимальным средним значением элементов-"+ str(A[aver , :]))
print("Среднее значение этой строки-"+str(mx)+ ","+ "номер этой строки-"+ str(aver+1))
