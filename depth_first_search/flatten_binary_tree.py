class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
- This solution uses O(n) extra space due to the nodes list.
"""
def flatten_O_n_space(root):
    nodes = []
    
    def preorder(node):
        if not node:
            return
        nodes.append(node)
        preorder(node.left)
        preorder(node.right)
        
    preorder(root)
    
    for i in range(len(nodes) - 1):
        nodes[i].left = None
        nodes[i].right = nodes[i + 1]
        
    nodes[-1].left = None
    nodes[-1].right = None

"""
Time Complexity: O(n)
Space Complexity: O(1)
This solution uses three steps:
1. Find the rightmost node in the left subtree
2. Connect the rightmost node to the right subtree
3. Move the left subtree to the right
"""
def flatten_O_1_space(root):
    def find_rightmost(node):
        while node.right:
            node = node.right
        return node
    
    while(root):
        if root.left:
            rightmost = find_rightmost(root.left)
            rightmost.right = root.right
            root.right = root.left
            root.left = None
        root = root.right
    

"""
Flatten binary tree to linked list recursively
Recursive (postorder)
Space Complexity: O(h) where h is the height of the tree
"""
def flatten_recursive(root):
    """
    Time Complexity: O(n) - Visits each node exactly once.
    Space Complexity: O(h) - Call stack max depth is the tree height.
    """
    def flatten_and_return_tail(node):
        if not node:
            return None
        
        left_tail = flatten_and_return_tail(node.left)
        right_tail = flatten_and_return_tail(node.right)
        
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
            
        return right_tail or left_tail or node
    
    flatten_and_return_tail(root)
    

"""
Recursive reverse postorder
"""
def flatten_recursive_reverse_postorder(root):
    """
    Time Complexity: O(n) - Visits each node exactly once.
    Space Complexity: O(h) - Call stack max depth is the tree height.
    """
    prev = None
    
    def dfs(node):
        nonlocal prev
        if not node:
            return
        
        dfs(node.right)
        dfs(node.left)
        
        node.right = prev
        node.left = None
        prev = node
    
    dfs(root)
    


import unittest

class TestFlattenBinaryTree(unittest.TestCase):
    def test_flatten_binary_tree_O_n_space(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        flatten_O_n_space(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertEqual(root.right.right.right.val, 4)
        self.assertEqual(root.right.right.right.right.val, 5)
        self.assertEqual(root.right.right.right.right.right.val, 6)

    def test_flatten_binary_tree_O_1_space(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        flatten_O_1_space(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertEqual(root.right.right.right.val, 4)
        self.assertEqual(root.right.right.right.right.val, 5)
        self.assertEqual(root.right.right.right.right.right.val, 6)
        
    def test_flatten_binary_tree_recursive(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        flatten_recursive(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertEqual(root.right.right.right.val, 4)
        self.assertEqual(root.right.right.right.right.val, 5)
        self.assertEqual(root.right.right.right.right.right.val, 6)
        
    def test_flatten_binary_tree_recursive_reverse_postorder(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        flatten_recursive_reverse_postorder(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertEqual(root.right.right.right.val, 4)
        self.assertEqual(root.right.right.right.right.val, 5)
        self.assertEqual(root.right.right.right.right.right.val, 6)
        

if __name__ == "__main__":
    unittest.main()


