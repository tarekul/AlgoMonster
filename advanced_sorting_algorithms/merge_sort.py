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