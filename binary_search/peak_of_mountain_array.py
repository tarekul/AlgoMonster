"""
A mountain array is defined as an array that

has at least 3 elements
has an element with the largest value called "peak", with index k. 
The array elements strictly increase from the first element to A[k], 
and then strictly decrease from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.

Find the index of the peak element. Assume there is only one peak element.

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: The largest element is 3, and its index is 3.
"""

from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    boundary_idx = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid+1]:
            boundary_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_idx

print(peak_of_mountain_array([0,1, 2, 3, 2, 1, 0]))
print(peak_of_mountain_array([0, 1, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 133, 132, 111, 0]))