def find_maximum(nums: list[int]) -> int:
    max_val = nums[0]
    
    for num in nums:
        if num > max_val:
            max_val = num
    
    return max_val


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = find_maximum(nums)
    print(res)
    
"""
Find Maximum
Write a function that finds the maximum element in an array of integers.

For example:

[3, 1, 4, 1, 5] → 5
[-10, -3, -7, -1] → -1
[42] → 42
Parameters:

nums: an array of integers (at least 1 element)
Return:

The maximum value in the array
"""