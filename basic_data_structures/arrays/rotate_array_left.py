def rotate_array_left(nums: list[int], k: int) -> list[int]:
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    n = len(nums)
    k = k % n
    # [1, 2, 3, 4, 5], k = 2
    reverse(0, k - 1) # [2, 1, 3, 4, 5]
    reverse(k, n - 1) # [2, 1, 5, 4, 3]
    reverse(0, n - 1) # [3, 4, 5, 1, 2]
    
    
    return nums
    

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = rotate_array_left(nums, k)
    print(" ".join(map(str, res)))
    
    
"""
Given an array of integers nums and an integer k, rotate the array to the left by k steps.
When you rotate an array to the left:
    1. The element at index 0 moves to the end of the array.
    2. All other elements shift one position to the left.
    3. This process repeats k times.

Example 1:
    - Input: nums = [1, 2, 3, 4, 5], k = 2
    - Output: [3, 4, 5, 1, 2]
    - Explanation: 
        - Rotate 1 step left: [2, 3, 4, 5, 1]
        - Rotate 2 steps left: [3, 4, 5, 1, 2]
Example 2:
    - Input: nums = [10, 20, 30, 40], k = 6
    - Output: [30, 40, 10, 20]
    - Explanation: 
        - Since the length is 4, rotating by 4 is the same as doing nothing.
        - Rotating by 6 is equivalent to rotating by 6 mod 4 = 2 steps.
Rotating by 6 is equivalent to rotating by 6 mod 4 = 2 steps.
"""