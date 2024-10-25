def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

print(insertion_sort([5, 3, 1, 2, 4]))

# space_complexity = O(1)
# time_complexity = O(n^2)

"""
This is a stable algorithm because it preserves the relative order of equal elements. 
Later elements will not be moved ahead of earlier equal elements.

This is an in-place algorithm because it sorts the array in place and does not require additional memory for another array.
"""