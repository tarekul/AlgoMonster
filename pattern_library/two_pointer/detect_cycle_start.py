"""
The Problem:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return None.

A cycle exists in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Wait, what makes this harder?
Detecting if a cycle simply exists is easy—you send your fast and slow pointers into the list. 
If there is a loop, the fast pointer will eventually lap the slow pointer, and they will crash into each other (slow == fast).

The hard part is figuring out exactly which node starts the loop. 
Because the fast pointer was jumping by two, the spot where they crash into each other is almost never the actual start of the loop. 
You have to write an algorithm that finds that exact entry node.

Examples
Example 1: Cycle exists

Input: 3 -> 2 -> 0 -> -4 (where -4 points back to 2)

Output: 2

Explanation: There is a cycle in the linked list, and the tail connects back to the second node (value 2).

Example 2: No cycle

Input: 1 -> 2 -> 3 -> 4 -> None

Output: None

Explanation: The list terminates, so there is no cycle.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def detect_cycle_start(head: Node) -> Node:
    if not head or not head.next:
        return None
    
    t1 = head
    t2 = head
    h = head
    
    while h and h.next:
        t1 = t1.next
        h = h.next.next
        
        if t1 is h:
            break
        
    if t1 is h:
        while t1 is not t2:
            t1 = t1.next
            t2 = t2.next
        return t1
    return None

import unittest

class TestCycleStart(unittest.TestCase):
    def _build_list_with_cycle(self, arr, cycle_index):
        """
        Builds a linked list from an array and connects the tail to the node 
        at 'cycle_index'. If cycle_index is -1, no cycle is created.
        Returns a tuple of (head_node, expected_cycle_start_node).
        """
        if not arr:
            return None, None
        
        head = Node(arr[0])
        curr = head
        cycle_node = head if cycle_index == 0 else None
        
        for i in range(1, len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
            if i == cycle_index:
                cycle_node = curr
        
        # If a cycle index was provided, attach the tail to it
        if cycle_node:
            curr.next = cycle_node
            
        return head, cycle_node
        
    def testHasCycle(self):
        # List: 0 -> 1 -> 6 -> 2 -> 3 -> 4 -> 5 -> (tail connects back to 2)
        # The start of the cycle is at index 3 (value 2)
        head, expected_start = self._build_list_with_cycle([0, 1, 6, 2, 3, 4, 5], 3)
        result = detect_cycle_start(head)
        
        self.assertIsNotNone(result)
        self.assertIs(result, expected_start)
        self.assertEqual(result.val, 2)
        
    def testNoCycle(self):
        # List: 1 -> 2 -> 3 -> 4 -> None
        head, _ = self._build_list_with_cycle([1, 2, 3, 4], -1)
        result = detect_cycle_start(head)
        
        self.assertIsNone(result)
        
    def testSingleCycle(self):
        # List: 1 -> (tail connects back to 1)
        # The node loops back onto itself
        head, expected_start = self._build_list_with_cycle([1], 0)
        result = detect_cycle_start(head)
        
        self.assertIsNotNone(result)
        self.assertIs(result, expected_start)
        self.assertEqual(result.val, 1)
        
        
if __name__ == "__main__":
    unittest.main()