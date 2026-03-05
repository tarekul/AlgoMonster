def intersection_of_arrays(nums1, nums2):
    count1: dict[int, int] = {}
    
    for num in nums1:
        count1[num] = count1.get(num, 0) + 1
    
    result = []
    for num in nums2:
        if num in count1 and count1[num] > 0:
            result.append(num)
            count1[num] -= 1
    
    return result

if __name__ == "__main__":
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    res = intersection_of_arrays(nums1, nums2)
    print(" ".join(map(str, res)))
    
    
"""
Intersection of Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1
Input

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
Output
An array of integers representing the intersection of the two arrays, preserving duplicate counts

[9,4]
"""

"""
Implementation
- Use a hash map to count occurrences of each element in the first array
- Iterate through the second array and check if each element exists in the hash map with a count > 0
- If found, add to result and decrement the count in the hash map
- Return the result array
"""