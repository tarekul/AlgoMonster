def bubble_sort(arr):
    swapped = False
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort([5, 3, 1, 2, 4]))

# space_complexity = O(1)
# time_complexity = O(n^2)

"""
This is a stable algorithm because a swap cannot cause an element to move past another one with the same value.

This is an in-place algorithm because it sorts the array in place and does not require additional memory for another array.
"""