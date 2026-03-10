def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
            
    return arr

numbers = [5, 4, 3, 2 , 1]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5]

"""
Insertion Sort already performs exceptionally well on already sorted or nearly sorted arrays.
It has a best-case time complexity of O(n) when the array is already sorted.

Input: [1, 2, 3, 4, 5]
Process: 
    - Pass 1: Check 2 -> already in correct position (2 > 1) 
    - Pass 2: Check 3 -> already in correct position (3 > 2)
    - Pass 3: Check 4 -> already in correct position (4 > 3)
    - Pass 4: Check 5 -> already in correct position (5 > 4)

Output: [1, 2, 3, 4, 5]

This characteristic makes insertion sort the algorithm of choice for maintaining sorted arrays 
when new elements arrive one at a time. Each insertion takes only O(n) time in the worst case, 
and often completes in O(1) time if the new element belongs at the end.

When to Use Insertion Sort
- Small datasets (typically n < 50)
- Nearly sorted data
- Insertion sort provides stable sorting (maintains relative order of equal elements)
"""
