def count_occurrences(nums: list[int], target: int) -> int:
    count = 0
    
    for num in nums:
        if num == target:
            count += 1
    
    return count    
    
if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = count_occurrences(nums, target)
    print(res)
    
"""
Count Occurrences
Write a function that counts how many times a target value appears in an array of integers.

For example:

[1, 2, 3, 2, 4, 2], target 2 → 3
[5, 5, 5, 5], target 5 → 4
[1, 2, 3], target 7 → 0 (not found)
Parameters:

nums: an array of integers
target: the value to count
Return:

The number of times target appears in the array

"""