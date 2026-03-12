def max_product_of_three(nums: list[int]) -> int:
    nums.sort(key=lambda x: abs(x), reverse=True)
    return nums[0] * nums[1] * nums[2]
    

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = max_product_of_three(nums)
    print(res)
    
    
"""
Maximum Product of Three
Given an integer array, find the maximum product of any three numbers.

This problem demonstrates why sorting helps reveal the solution structure. With negative numbers in the array, the maximum product isn't always the three largest numbers.

Input
nums: a list of integers (may contain negative numbers)
Output
An integer representing the maximum product of any three numbers

Examples
Example 1:
Input: nums = [1, 2, 3, 4]

Output: 24

Explanation:

All numbers are positive
Maximum product: 4 * 3 * 2 = 24
Example 2:
Input: nums = [-4, -3, 1, 2, 3]

Output: 36

Explanation:

Two large negative numbers multiplied together give a positive result
Option 1: 3 * 2 * 1 = 6
Option 2: (-4) * (-3) * 3 = 36
Maximum: 36
Example 3:
Input: nums = [-10, -10, 5, 2]

Output: 500

Explanation:

Option 1: 5 * 2 * (-10) = -100
Option 2: (-10) * (-10) * 5 = 500
Maximum: 500
"""
