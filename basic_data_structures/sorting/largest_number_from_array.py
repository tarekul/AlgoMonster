from functools import cmp_to_key

def largest_number_from_array(nums: list[int]) -> str:
    # Convert integers to strings
    str_nums = [str(num) for num in nums]

    def compare(a, b):
        if a + b > b + a:
            return -1  # a comes before b
        elif a + b < b + a:
            return 1   # b comes before a
        else:
            return 0   # equal

    # Sort using custom comparator
    str_nums.sort(key=cmp_to_key(compare))

    # Handle edge case: all zeros
    if str_nums[0] == '0':
        return '0'

    # Concatenate sorted strings
    return ''.join(str_nums)
    

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = largest_number_from_array(nums)
    print(res)
    
"""
Problem Description
Given an array of non-negative integers, arrange them to form the largest possible number. The result should be returned as a string.

Input: An array of non-negative integers

Output: A string representing the largest number that can be formed by concatenating the array elements in some order

Examples:

Input: [3, 30, 34, 5, 9]
Output: "9534330"
Explanation: Arrange numbers to form 9-5-34-3-30.
             This gives 9534330, which is larger than any other arrangement.

Input: [10, 2]
Output: "210"
Explanation: "210" is larger than "102".

Input: [0, 0, 0]
Output: "0"
Explanation: When all numbers are zero, return "0" instead of "000".

Input: [121, 12]
Output: "12121"
Explanation: "12121" is larger than "12112".
             Comparing: "121" + "12" = "12112" vs "12" + "121" = "12121"
"""