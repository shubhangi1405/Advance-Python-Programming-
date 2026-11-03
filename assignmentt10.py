import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("Slicing (first 5 elements):", arr[:5])
print("Slicing (last 5 elements):", arr[5:])
print("Slicing (alternate elements):", arr[::2])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5
print("After Broadcasting:", arr)
