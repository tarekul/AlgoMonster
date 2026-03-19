def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    nums1.extend([0] * n)
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    
        
    return nums1

import unittest

class TestMerge(unittest.TestCase):
    def test_merge(self):
        nums1 = [1, 2, 3]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])
        
    def test_merge_empty(self):
        nums1 = []
        m = 0
        nums2 = []
        n = 0
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [])

if __name__ == "__main__":
    unittest.main()

