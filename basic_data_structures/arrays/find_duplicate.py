"""
Given an array of n + 1 integers where each value is between 1 and n, and exactly one number is repeated. Find that duplicate.
Constraints: Cannot modify array, O(1) extra space only
"""

def find_duplicate(nums):
    slow = 0
    slow2 = 0
    fast = 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
        
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow

import unittest

class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        nums = [1,6,3,4,5,2,2]
        self.assertEqual(find_duplicate(nums), 2)
        
if __name__ == "__main__":
    unittest.main()