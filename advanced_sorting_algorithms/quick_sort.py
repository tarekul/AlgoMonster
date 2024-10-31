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
