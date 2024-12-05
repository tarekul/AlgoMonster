'''
Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree, find its max depth. 
Here, we define the length of the path to be the number of edges on that path, not the number of nodes.
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    def dfs(root):
        if root is None:
            return 0
    
        left = dfs(root.left)
        right = dfs(root.right)
    
        return 1 + max(left,right)
    return dfs(root) - 1 if root else 0

root = Node(1)
child1 = Node(2)
child2 = Node(3)

root.left = child1
root.right = child2

sub_child1 = Node(4)
sub_child2 = Node(5)
sub_child3 = Node(6)
child1.left = sub_child1
child2.left = sub_child2
child2.right = sub_child3

print(tree_max_depth(root))