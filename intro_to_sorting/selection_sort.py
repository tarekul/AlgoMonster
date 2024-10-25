def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 3, 1, 2, 4]))

# space_complexity = O(1)
# time_complexity = O(n^2)

"""
This is an unstable algorithm because an earlier element may be moved behind a later equal element.

This is an in-place algorithm because it sorts the array in place and does not require additional memory for another array.
"""