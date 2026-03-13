def quick_sort(arr, low, high):
    if low < high:
        p_idx = partition(arr, low, high)
        quick_sort(arr, low, p_idx - 1)
        quick_sort(arr, p_idx + 1, high)
        
def partition(arr, low, high):
    pivot = arr[low + (high-low) // 2]
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
    quick_sort(arr, 0, len(arr) - 1)
    print(" ".join(map(str, arr)))
    
"""
Quick Sort:
- Pick a pivot element
- Partition the array into 3 parts:
  - Elements less than the pivot
  - Elements equal to the pivot
  - Elements greater than the pivot
- Recursively sort the left and right parts

Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n)
"""