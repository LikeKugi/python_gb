import numpy as np
from collections import Counter

arr = np.random.randint(0, 15, (4, 4))
print(arr)

unique, counts = np.unique(arr, return_counts=True)
print(unique); print(counts)

max_count = np.max(counts)
index_max_count = np.argmax(counts)

print(f'max frequency: {counts[index_max_count]}')
print(f'max frequency number: {unique[index_max_count]}')
