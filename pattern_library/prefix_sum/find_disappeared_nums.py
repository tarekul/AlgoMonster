class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Return every value in [1, n] that does not appear in nums.
        for e in nums:
            idx = abs(e) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result

s = Solution()
print(s.findDisappearedNumbers([2,3,2,1,5]))
print(s.findDisappearedNumbers([1,1,1,1,1]))