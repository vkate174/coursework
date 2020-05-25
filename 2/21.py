# 21
# описание: Создать квадратную матрицу A, имеющую N строк и N столбцов со
# случайными элементами. Каждой паре элементов, симметричных
# относительно главной диагонали (ближайшие к главной), присвоить
# значения, равные полусумме этих симметричных значений (элементы
# главной диагонали имеют индексы от [0,0] до [N,N]).


import numpy as np

N = 4


A = np.random.randint(low=-9, high=10, size=(N, N)).astype(float)
print("Матрица:\r\n{}".format(A))

diagonal_elements = [np.diagonal(A, i) for i in [1, -1]]
print("Элементы, расположенные параллельно главной диагонали:")
print(diagonal_elements)

values = (diagonal_elements[0] + diagonal_elements[1])/2
print(values)

rng = np.arange(N-1)
A[rng, rng+1] = values[rng]
A[rng+1, rng] = values[rng]

print("Полученная матрица:\r\n{}".format(A))
