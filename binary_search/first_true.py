"""
This function finds the first True value in a sorted boolean array.
The array is divided into two sections:
- Left section: all False values
- Right section: all True values

The function returns the index of the first True value, or -1 if no True exists.

Time complexity: O(log n) since we use binary search to find the boundary
Space complexity: O(1) since we only store a few variables

Example:
Input: [False, False, True, True, True]
Output: 2 (index of first True)
"""



from typing import List

def find_boundary(arr: List[bool]) -> int:
    boundary_idx = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == True:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_idx

print(find_boundary([False, False, True, True, True]))
print(find_boundary([False, False]))
print(find_boundary([True, True, True, True]))