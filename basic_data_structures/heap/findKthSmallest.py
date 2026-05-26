def findKthSmallest(nums, k):
    max_heap = []
    
    for num in nums:
        heapify_up(max_heap, num)
        if len(max_heap) > k:
            heapify_down(max_heap)
    
    return max_heap[0]
        
def heapify_up(max_heap, num):
    max_heap.append(num)
    
    current_idx = len(max_heap) - 1
    
    while current_idx > 0:
        parent_idx = (current_idx - 1) // 2
        
        if max_heap[current_idx] > max_heap[parent_idx]:
            max_heap[current_idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[current_idx]
            current_idx = parent_idx
        else:
            break
    
def heapify_down(max_heap):
    if not max_heap:
        return
    
    # 1. Swap the root (the maximum element) with the last element in the array
    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    
    # 2. Remove the old root from the heap entirely
    max_heap.pop()
    
    # 3. Sift down: move the new root down to its proper place
    current_idx = 0
    n = len(max_heap)
    
    while True:
        left_child_idx = 2 * current_idx + 1
        right_child_idx = 2 * current_idx + 2
        largest_idx = current_idx
        
        if left_child_idx < n and max_heap[left_child_idx] > max_heap[largest_idx]:
            largest_idx = left_child_idx
        
        if right_child_idx < n and max_heap[right_child_idx] > max_heap[largest_idx]:
            largest_idx = right_child_idx
        
        if largest_idx == current_idx:
            break
        
        max_heap[current_idx], max_heap[largest_idx] = max_heap[largest_idx], max_heap[current_idx]
        current_idx = largest_idx
    



import unittest

class TestFindKthSmallest(unittest.TestCase):
    def testFindKthSmallest(self):
        self.assertEqual(findKthSmallest([3, 2, 1, 5, 6, 4], 2), 2)
        self.assertEqual(findKthSmallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 3)
        
if __name__ == "__main__":
    unittest.main()