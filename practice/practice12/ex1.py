import numpy as np


def search(nums, target) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    else:
        return start


arr = 10 + 3.5 * np.random.randn(6)

print(arr)

arr_mean = np.mean(arr)
print(arr_mean)

arr = np.sort(arr, axis=None)
print(arr)

print(index := search(list(arr), 10))
print(arr[index])
