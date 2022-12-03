import numpy as np
from matplotlib import pyplot as plt

arr1 = np.array([56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63])
arr2 = np.array([66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72])
arr3 = np.array([89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96])

cr1 = np.corrcoef(arr1, arr2)
cr2 = np.corrcoef(arr2, arr3)
cr3 = np.corrcoef(arr3, arr1)

matrix = np.array([*arr1, *arr2, *arr3])
np.reshape(matrix, (3, len(arr1)))
cr_all = np.corrcoef(matrix)

print(cr_all)

print(cr1, cr2, cr3)

plt.plot(arr1, 'r')
plt.plot(arr2, 'g')
plt.plot(arr3, 'b')
plt.show()
