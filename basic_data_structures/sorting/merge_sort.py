def merge_sort(arr):
  if len(arr) <= 1:
    return arr
    
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  
  return merge(left, right)
  
def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right): 
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else: 
      result.append(right[j])
      j += 1
  
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result
    

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    sorted_arr = merge_sort(arr)
    print(" ".join(map(str, sorted_arr)))
    
"""
Merge Sort
Given an array of integers, sort the elements in the array in ascending order. The merge sort algorithm should be used to solve this problem.

Examples
1, 3, 5, 2, 4, 6 -> 1, 2, 3, 4, 5, 6

Constraints
The length of the array is between [0, 5000]
The values of the elements in the array is between [-5000, 5000]
"""