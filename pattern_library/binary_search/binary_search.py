"""
Given a sorted integer array nums (ascending order, no duplicates) and a value target, return the index of target if it is in the array, or -1 if it is not.
"""


class Solution:
    def search_i(self, nums: list[int], target: int) -> int:
        # Return the index of target in the sorted array nums, or -1 if absent.
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1
    
    def search_r(self, nums: list[int], target: int) -> int:
        # Return the index of target in the sorted array nums, or -1 if absent.
        def binary_search(low, high):
            if low > high:
                return -1
            
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, high)
            else:
                return binary_search(low, mid - 1)
        
        return binary_search(0, len(nums) - 1)

s = Solution()
print(s.search_i([1,2,3,4,5], 3))
print(s.search_i([1,2,3,4,5], 6))
print(s.search_r([1,2,3,4,5], 3))
print(s.search_r([1,2,3,4,5], 6))
