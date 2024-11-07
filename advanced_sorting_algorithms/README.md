Merge sort requires a good understanding of recursion and Quick sort requires basic two pointers algorithm.

## Merge Sort


The idea of merge sort is divide and conquer. We divide the array into two almost equally, sort them (usually another merge sort) and merge the two sorted lists into one. To merge the two sorted lists, have two pointers pointing towards the bottom of the two lists, and in each step, add the smaller element from those two into the list and move the pointer of that item up by one until elements from both lists are fully added.

```other
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)

def merge(arr1, arr2):
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

print(merge_sort([5,3,1,2,4]))

"""
time complexity: O(n log n)
The main idea of merge sort is to divide the list in half until we are left with sub-lists of size 1. 
If we start with n elements, the first split gets us two lists with size n/2. The second split would give us
four lists with size n/4. Continuing this pattern we woud get n lists with size 1. The number of times we would is O(log(n))
because log(n) represents how many times we can divide a list by 2

Once everything is split to merge two lists of size n requires O(n) operations in the worst case.

Merge sort is stable because if two elements are the same in the same list or two different lists the first one will be inserted first
Merge sort is not in place because of the additional arrays.
"""
```


## Quick Sort


The idea of quick sort is as follows: we select an arbitary element in the list (known as the "pivot"), and we swap the elements in the list into two sides: a side where all the elements are smaller than the pivot and a side where elements are larger than the pivot. 

After grouping them this way we swap the pivot with the first element of the side larger or equal to the pivot. This way each element left of the pivot is smaller than it, and each element on the right is greater or equal to it. 

```other
def sort_list_interval(arr, start, end):
    if end - start <= 1:
        return
    
    pivot = arr[end - 1]
    start_ptr, end_ptr = start, end - 1

    while start_ptr < end_ptr:
        while arr[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        while arr[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1
        
        arr[start_ptr], arr[end_ptr] = arr[end_ptr], arr[start_ptr]

    arr[end - 1], arr[end_ptr] = arr[end_ptr], arr[end - 1]

    sort_list_interval(arr, start, start_ptr)
    sort_list_interval(arr, start_ptr + 1, end)

def quick_sort(arr):
    sort_list_interval(arr, 0, len(arr))
    return arr

print(quick_sort([5, 3, 1, 2, 4]))

"""
Quick Sort Algorithm

This implementation uses the last element as the pivot and partitions
the array around it. Elements smaller than the pivot are moved to the left
side and elements greater than or equal to pivot are moved to the right side.

Time Complexity:
- Average Case: O(n log n) because on each recursive call divide list into two roughly equal halves then sort each half
- Worst Case: O(n^2) when array is already sorted because if list is sorted we are recursively calling list n times and sorting each list of size n-1.

Space Complexity: O(log n) due to recursive call stack
"""

```

