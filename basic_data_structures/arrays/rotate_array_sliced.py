def rotate_array(nums: list[int], k: int) -> list[int]:
    if not nums or k == 0:
        return nums[:]
    
    n = len(nums)
    
    k = k % n
    
    return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = rotate_array(nums, k)
    print(" ".join(map(str, res)))
    
"""
Rotate Array
Write a function that rotates an array k positions to the right.

For example:

[1, 2, 3, 4, 5], k = 2 → [4, 5, 1, 2, 3]
[1, 2, 3], k = 4 → [3, 1, 2] (k > array length wraps around)
[1, 2, 3, 4], k = 0 → [1, 2, 3, 4] (no rotation)
Parameters:

nums: an array of integers
k: number of positions to rotate right
Return:

A new array with elements rotated k positions to the right
"""