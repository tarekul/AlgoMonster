def remove_element(nums: list[int], target: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != target:
            nums[k] = nums[i]
            k += 1
    
    return k
    
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length. It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

"""

import unittest

class TestRemoveElement(unittest.TestCase):
    def test_basic_case(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        
        k = remove_element(nums, val)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)
    
    def test_no_matches(self):
        nums = [1, 2, 3, 4]
        val = 5
        k = remove_element(nums, 5)
        self.assertEqual(k, 4)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3, 4])

    def test_all_matches(self):
        nums = [1, 1, 1]
        val = 1
        k = remove_element(nums, 1)
        self.assertEqual(k, 0)

    def test_empty_list(self):
        nums = []
        k = remove_element(nums, 0)
        self.assertEqual(k, 0)
        
if __name__ == "__main__":
    unittest.main()