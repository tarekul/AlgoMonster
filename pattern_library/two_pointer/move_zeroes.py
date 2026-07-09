class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        # Move all zeros to the end while preserving the order of non-zeros.
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
            
        
if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([4,  0, 1, 0, 7, 3]))
    print(s.moveZeroes([0, 0, 0, 0, 1]))
    print(s.moveZeroes([0, 0, 0, 1, 8, 4, 3, 2]))
    print(s.moveZeroes([4, 5, 6, 0, 2, 0, 0, 9, 4]))
    