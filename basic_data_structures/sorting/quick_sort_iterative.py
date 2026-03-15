def quick_sort_iterative(arr, low, high):
    stack = []
    stack.append((low, high))
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            p_idx = partition(arr, low, high)
            stack.append((low, p_idx - 1))
            stack.append((p_idx, high))
        
def partition(arr, low, high):
    pivot = arr[low + (high - low) // 2]
    i = low
    j = high
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
            
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    return i




if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    quick_sort_iterative(arr, 0, len(arr) - 1)
    print(" ".join(map(str, arr)))