import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Max = A.max()
print(Max)
A = A / Max

print("Новая матрица:\r\n{}\n".format(A))
