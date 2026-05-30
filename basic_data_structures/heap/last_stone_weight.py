"""
You are given an array stones of positive integer weights. On each turn, choose the two heaviest stones and smash them together. Let their weights be a and b with a >= b. Then:

If a == b, both stones are destroyed.
If a != b, the stone of weight b is destroyed and the stone of weight a has its weight replaced with a - b.
At the end, there is at most one stone remaining. Return the weight of that stone, or 0 if no stones remain.
"""

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []
        for s in stones:
            self.push(max_heap, s)
            
        while len(max_heap) > 1:
            first = self.pop(max_heap)
            second = self.pop(max_heap)
            if first != second:
                self.push(max_heap, first - second)
        return self.pop(max_heap) if max_heap else 0
    
    def push(self, max_heap: list[int], val: int):
        max_heap.append(val)
        self.sift_up(max_heap, len(max_heap) - 1)
        
    def sift_up(self, max_heap: list[int], idx: int):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if max_heap[idx] > max_heap[parent_idx]:
                max_heap[idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[idx]
                idx = parent_idx
            else:
                break
    def pop(self, max_heap: list[int]):
        if not max_heap:
            return None
        if len(max_heap) == 1:
            return max_heap.pop()
        
        max_val = max_heap[0]
        max_heap[0] = max_heap.pop()
        self.sift_down(max_heap, 0)
        return max_val
    
    def sift_down(self, max_heap: list[int], idx: int):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest_idx = idx
            
            if left_child_idx < len(max_heap) and max_heap[left_child_idx] > max_heap[largest_idx]:
                largest_idx = left_child_idx
            
            if right_child_idx < len(max_heap) and max_heap[right_child_idx] > max_heap[largest_idx]:
                largest_idx = right_child_idx
            
            if largest_idx == idx:
                break
            
            max_heap[idx], max_heap[largest_idx] = max_heap[largest_idx], max_heap[idx]
            idx = largest_idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(solution.lastStoneWeight([10, 4, 6]))
    print(solution.lastStoneWeight([5]))
    print(solution.lastStoneWeight([]))
    
