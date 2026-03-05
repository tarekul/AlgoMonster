def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    merged = []
    i = 0
    j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    if i < len(nums1):
        merged.extend(nums1[i:])
        
    if j < len(nums2):
        merged.extend(nums2[j:])
    
    return merged

if __name__ == "__main__":
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    res = merge_sorted_arrays(nums1, nums2)
    print(" ".join(map(str, res)))
    
"""
Merge Sorted Arrays
Write a function that merges two sorted arrays into one sorted array.

For example:

[1, 3, 5] and [2, 4, 6] → [1, 2, 3, 4, 5, 6]
[1, 2, 3] and [] → [1, 2, 3]
[] and [4, 5, 6] → [4, 5, 6]
Parameters:

nums1: a sorted array of integers
nums2: a sorted array of integers
Return:

A new sorted array containing all elements from both arrays
"""