"""
Given a sorted array of distinct integers nums and a target value target, 
return the index where target would be found if it exists, 
or the index where it would be inserted to keep the array sorted if it does not.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Return the index where target is (or would be inserted).
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    
s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([6,7,8,9], 5))
print(s.searchInsert([2,7,8,9], 5))

