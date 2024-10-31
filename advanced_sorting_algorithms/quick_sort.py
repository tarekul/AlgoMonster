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
- Average Case: O(n log n)
- Worst Case: O(n^2) when array is already sorted
- Best Case: O(n log n)

Space Complexity: O(log n) due to recursive call stack
"""
