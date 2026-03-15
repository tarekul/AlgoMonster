def quick_sort(arr, low, high):
    if low < high:
        p_idx = partition(arr, low, high)
        quick_sort(arr, low, p_idx - 1)
        quick_sort(arr, p_idx, high)
        
def partition(arr, low, high):
    pivot = arr[low + (high - low) // 2]
    print(f"\n--- New Partition | Range: {arr[low:high+1]} | Pivot: {pivot} ---")
    i = low
    j = high
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
            
        if i <= j:
            print(f"Swapping {arr[i]} and {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Current List: {arr}")
            i += 1
            j -= 1
    
    return i
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(f"Original: {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"\nFinal Sorted List: {arr}")
    
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

Example:
    Input: [3,1,4,2]
    Output: [1,2,3,4]
    
    quick_sort(arr, 0, 3)
    partition(arr, 0, 3) -> i = 1
    
    quick_sort(arr, 0, 0)
    quick_sort()
        
    
"""