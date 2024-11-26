import random

# Generate random integers
random.seed(40)
data = [random.randint(0, 100) for _ in range(50)]

# Naive sorting using Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Sort the data
sorted_data = bubble_sort(data)
print("Original Data:", data)
print("Sorted Data (Naive Method):", sorted_data)
