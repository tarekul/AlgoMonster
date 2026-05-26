class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def _to_list(arr):
    """Build a linked list of ListNodes from a Python list. Returns the head."""
    head = None
    for v in reversed(arr):
        head = ListNode(v, head)
    return head

def _from_list(head):
    """Walk a linked list of ListNodes and return its values as a Python list."""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

def _build_cyclic(values, pos):
    head = _to_list(values)
    if head is None or pos == -1:
        return head
    # Find the tail and the node at index pos.
    tail = head
    while tail.next is not None:
        tail = tail.next
    node = head
    for _ in range(pos):
        node = node.next
    tail.next = node
    return head


class Solution:
    def hasCycle(self, values: list[int], pos: int) -> bool:
        head = _build_cyclic(values, pos)

        if not head or not head.next:
            return False
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
        return False
        

import unittest

class TestCyclicDetection(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertTrue(s.hasCycle([3, 2, 0, -4], 1))
    def testNoCycle(self):
        s = Solution()
        self.assertFalse(s.hasCycle([1, 2, 3], -1))
    def testSingleCycle(self):
        s = Solution()
        self.assertTrue(s.hasCycle([1, 2], 0))
        
if __name__ == "__main__":
    unittest.main()



