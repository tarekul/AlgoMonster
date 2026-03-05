def two_sum(arr: list[int], target: int) -> list[int]:
    s: dict[int, int] = {}
    for i, num in enumerate(arr):
        if target - num in s:
            return [s[target - num], i]
        s[num] = i
    
    return []
        

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr, target)
    print(" ".join(map(str, res)))
    
"""
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""