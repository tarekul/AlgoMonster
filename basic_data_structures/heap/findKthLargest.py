import heapq

def findKthLargest(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

import unittest

class TestFindKthLargest(unittest.TestCase):
    def testFindKthLargest(self):
        self.assertEqual(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        
if __name__ == "__main__":
    unittest.main()