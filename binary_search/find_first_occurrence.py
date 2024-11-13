"""
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
Output: 1

The feasible function is arr[mid] == target

For example:
arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100], target = 3

At mid=4 (value 3):
3 == 3 returns True, so we store index 4 and search left half
At mid=2 (value 3):
3 == 3 returns True, so we store index 2 and search left half
At mid=1 (value 3):
3 == 3 returns True, so we store index 1 and search left half
At mid=0 (value 1):
1 == 3 returns False, so we search right half

Final answer is index 1, the first occurrence of target

"""

from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    boundary_idx = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_idx

print(find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))
print(find_first_occurrence([2, 3, 5, 7, 11, 13, 17, 19], 6))