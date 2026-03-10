def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
    

numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 64]

"""
Swap Efficiency
- Only one swap per pass (n-1 swaps at most)
- More efficient than bubble sort which swaps every time

When to Use Selection Sort
- Small datasets (n < 50)
- Memory writes are costly
- When minimizing number of swaps is important
"""