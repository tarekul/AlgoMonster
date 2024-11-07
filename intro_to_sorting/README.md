### Insertion Sort


The idea of insertion sort is for each item in the list, we insert the item into the "sorted" list by swapping with the item before it until the item is smaller than the current item.

```other
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
```


### Selection Sort


The idea of selection sort is for each index find the minimum element in the unsorted list and add it to the sorted list.

```other
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
```


### Bubble Sort


The idea of bubble swap is this: for each pass, we set a pointer at the first element of the list. For each cycle, we compare it to the next element in the list and swap them if the current item is greater, then move the pointer by 1 until we reach the end of the list. Naturally the largest element will "bubble" to the end and for each interval we consider the interval exluding the last element of the previous interval. We include the swapped boolean to stop when we encounter no swaps during a pass. This means the list is sorted.

```other
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
```

