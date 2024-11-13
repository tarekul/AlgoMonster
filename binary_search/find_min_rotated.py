"""
A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: The smallest element is 10, and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7

Explanation: The smallest element is 2, and its index is 7.

The feasible function is arr[mid] <= arr[-1]

For example:
arr = [30, 40, 50, 10, 20]

At mid=2 (value 50):
50 <= 20 returns False, so we search right half
At mid=3 (value 10):
10 <= 20 returns True, so we store index 3 and search left half
At mid=2 (value 50):
50 <= 20 returns False, so we search right half

Final answer is index 3, the minimum element

The key insight is that in a rotated sorted array, all elements <= the last element must be in the right portion after rotation, while all elements > the last element must be in the left portion. This creates our monotonic function.

"""

from typing import List

def find_min_rotated(arr: List[int]) -> int:
    boundary_idx = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_idx

print(find_min_rotated([30, 40, 50, 10, 20]))
print(find_min_rotated([3, 5, 7, 11, 13, 17, 19, 2]))