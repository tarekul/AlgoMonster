"""
This function finds the first element in a sorted array that is not smaller than (>=) the target value.
The array is sorted in increasing order.
Returns the index of the first element >= target.

Time complexity: O(log n) since we use binary search
Space complexity: O(1) since we only store a few variables

Example:
Input: arr=[1,3,3,5,8,8,10], target=2
Output: 1 (index of first element >= 2, which is 3)

Input: arr=[2,3,5,7,11,13,17,19], target=6  
Output: 3 (index of first element >= 6, which is 7)

The feasible function is arr[mid] >= target

For example:
arr = [1,3,3,5,8,8,10], target = 2

At mid=3 (value 5):
5 >= 2 returns True, so we store index 3 and search left half
At mid=1 (value 3): 
3 >= 2 returns True, so we store index 1 and search left half
At mid=0 (value 1):
1 >= 2 returns False, so we search right half

Final answer is index 1, the first element >= target

"""


from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    boundary_idx = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_idx

print(first_not_smaller([1, 3, 3, 5, 8, 8, 10], 2))
print(first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6))