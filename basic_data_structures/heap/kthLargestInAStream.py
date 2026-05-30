class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.push(num)
            if len(self.min_heap) > self.k:
                self.pop()
    
    def add(self, val: int) -> int:
        # If the heap isn't full yet, just push
        if len(self.min_heap) < self.k:
            self.push(val)
        else:
            # Otherwise, push the new value and instantly pop the smallest
            self.pushpop(val)
            
        # The root of the min-heap is always the kth largest element
        return self.min_heap[0]
    
    def push(self, val: int):
        self.min_heap.append(val)
        current_idx = len(self.min_heap) - 1
        
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            
            if self.min_heap[current_idx] < self.min_heap[parent_idx]:
                self.min_heap[current_idx], self.min_heap[parent_idx] = self.min_heap[parent_idx], self.min_heap[current_idx]
                current_idx = parent_idx
            else:
                break
            
    def pushpop(self, val: int):
        if self.min_heap and val > self.min_heap[0]:
            popped = self.min_heap[0]
            self.min_heap[0] = val
            self._sift_down(0)
            return popped
        return val
            
    def pop(self):
        if not self.min_heap:
            return None
        
        # Swap root with last element
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        
        # Remove the last element (which was the root)
        root = self.min_heap.pop()
        
        # Sift down the new root to maintain heap property
        self._sift_down(0)
        
        return root
    
    def _sift_down(self, idx: int):
        n = len(self.min_heap)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            
            if left < n and self.min_heap[left] < self.min_heap[smallest]:
                smallest = left
            if right < n and self.min_heap[right] < self.min_heap[smallest]:
                smallest = right
                
            if smallest == idx:
                break
                
            self.min_heap[idx], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[idx]
            idx = smallest
    
class Solution:
    def runKthLargestOps(self, k: int, nums: list[int], ops: list[str], vals: list[list[int]]) -> list[int]:
        k1 = KthLargest(k, nums)
        out = []
        for op, args in zip(ops, vals):
            out.append(getattr(k1, op)(*args))
        return out
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.runKthLargestOps(3, [4, 5, 8, 2], ["add", "add", "add", "add"], [[3], [5], [10], [9]]))
    print(solution.runKthLargestOps(5, [1, 2], ["add", "add", "add", "add"], [[3], [4], [5], [6]]))