import numpy as np

matrix = np.random.randint(0, 2, (3, 10))
print(matrix)
print(~matrix.any(axis=0))