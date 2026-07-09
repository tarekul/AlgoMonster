class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Return the largest average of any length-k contiguous window of nums.
        curr = sum(nums[:k])
        best = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            if curr > best:
                best = curr
        return best / k

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([2,4,1,5,3], 2))
    print(s.findMaxAverage([-1,-2,-3,-4,-5], 2))