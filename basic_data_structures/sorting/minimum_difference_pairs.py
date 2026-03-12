def minimum_difference_pairs(arr: list[int]) -> list[list[int]]:
    arr.sort()
    res = []
    min_diff = float('inf')
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            res.append([arr[i-1], arr[i]])
        elif arr[i] - arr[i-1] < min_diff:
            min_diff = arr[i] - arr[i-1]
            res = [[arr[i-1], arr[i]]]
    
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = minimum_difference_pairs(arr)
    for row in res:
        print(" ".join(map(str, row)))

"""
Problem Description
Given an array of integers, find all pairs of adjacent elements (after sorting) that have the minimum absolute difference. Return these pairs in sorted order.

Input: An array of integers

Output: A list of pairs [a, b] where a < b and |b - a| is the minimum absolute difference in the array

Examples:

Input: [4, 2, 1, 3]
Output: [[1, 2], [2, 3], [3, 4]]
Explanation: After sorting: [1, 2, 3, 4]
             All adjacent pairs have difference 1 (the minimum)

Input: [1, 5, 3, 19, 18, 25]
Output: [[18, 19]]
Explanation: After sorting: [1, 3, 5, 18, 19, 25]
             Minimum difference is 1, only the pair (18, 19) has this difference

Input: [5, 5, 5, 5]
Output: [[5, 5], [5, 5], [5, 5]]
Explanation: After sorting: [5, 5, 5, 5]
             All adjacent pairs have difference 0 (the minimum)
"""