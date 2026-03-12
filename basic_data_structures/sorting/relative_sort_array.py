from collections import Counter

def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = Counter(arr1)
    res = []
    
    for num in arr2:
        res.extend([num] * counts[num])
        del counts[num]
        
    for num in sorted(counts.keys()):
        res.extend([num] * counts[num])
    
    return res

if __name__ == "__main__":
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    res = relative_sort_array(arr1, arr2)
    print(" ".join(map(str, res)))

"""
Problem Description
Given two arrays arr1 and arr2, sort arr1 so that the elements appear in the same relative order as they appear in arr2. Elements that don't appear in arr2 should be placed at the end in ascending order.

Input: Two arrays of integers

arr1: Array to be sorted
arr2: Array defining the ordering
Output: Array arr1 sorted according to the order in arr2

Examples:

Input: arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6]
Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
Explanation: Elements from arr2 appear first in that order: 2 (×3), 1 (×1), 4 (×1), 3 (×2), 9 (×1), 6 (×1)
             Elements not in arr2 appear last in ascending order: 7, 19
"""