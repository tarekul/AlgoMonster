def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    result = quick_sort(arr)
    print(" ".join(map(str, result)))
    
"""
Quick Sort:
- Pick a pivot element
- Partition the array into 3 parts:
  - Elements less than the pivot
  - Elements equal to the pivot
  - Elements greater than the pivot
- Recursively sort the left and right parts
"""