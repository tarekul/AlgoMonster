class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def get_intersection_node(headA: Node, headB: Node) -> Node:
    if not headA or not headB:
        return None
    
    pA = headA
    pB = headB
    
    while pA is not pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA


import unittest

class TestIntersection(unittest.TestCase):
    def _build_list(self, arr1, arr2, inter1_idx, inter2_idx):
        if not arr1 and not arr2:
            return None, None, None
            
        # 1. Create nodes and store them in Python lists for instant index access
        nodes1 = [Node(val) for val in arr1]
        nodes2 = [Node(val) for val in arr2]
        
        # 2. Link the nodes together sequentially
        for i in range(len(nodes1) - 1):
            nodes1[i].next = nodes1[i+1]
            
        for i in range(len(nodes2) - 1):
            nodes2[i].next = nodes2[i+1]
            
        head1 = nodes1[0] if nodes1 else None
        head2 = nodes2[0] if nodes2 else None
        intersection_node = None
        
        # 3. Form the intersection using direct array access
        if inter1_idx >= 0 and inter2_idx >= 0:
            intersection_node = nodes1[inter1_idx]
            
            if inter2_idx == 0:
                head2 = intersection_node
            else:
                # Instantly grab the node right before the intersection and point it
                nodes2[inter2_idx - 1].next = intersection_node
                
        return head1, head2, intersection_node

    def test_standard_intersection(self):
        # List A: 4 -> 1 -> 8 -> 4 -> 5
        # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
        # Intersects at node with value '8' (index 2 in A, index 3 in B)
        headA, headB, expected = self._build_list([4,1,8,4,5], [5,6,1,8,4,5], 2, 3)
        result = get_intersection_node(headA, headB)
        
        self.assertIsNotNone(result)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 8)

    def test_no_intersection(self):
        # List A: 2 -> 6 -> 4
        # List B: 1 -> 5
        # Indices are -1 to indicate no intersection
        headA, headB, expected = self._build_list([2,6,4], [1,5], -1, -1)
        result = get_intersection_node(headA, headB)
        
        self.assertIsNone(result)
        self.assertIs(result, expected)
        
    def test_intersection_at_head(self):
        # List A: 1 -> 2 -> 3
        # List B is identical to List A, merging at the very first node
        headA, headB, expected = self._build_list([1,2,3], [1,2,3], 0, 0)
        result = get_intersection_node(headA, headB)
        
        self.assertIsNotNone(result)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 1)

if __name__ == "__main__":
    unittest.main()
