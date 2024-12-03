'''
A tree is a type of graph data structure composed of nodes and edges. It's main properties are:
- Each node has exactly one parent (except for the root node which has no parent)
- Each node can have multiple children
- Has N - 1 edges where N is the number of nodes in the tree
- There are no cycles (a node cannot be its own ancestor)
- All nodes are connected (there is a path from root to every node)
- A binary tree specifically has at most 2 children per node
'''


class binary_node:
    def __init__(self, val): 
        self.val = val
        self.left = None
        self.right = None
        
class tree_node:
    def __init__(self, val):
        self.val = val
        self.children = []
        
root = binary_node(1)
child1 = binary_node(2)
child2 = binary_node(3)

root.left = child1
root.right = child2

sub_child1 = binary_node(4)
sub_child2 = binary_node(5)
sub_child3 = binary_node(6)
child1.left = sub_child1
child2.left = sub_child2
child2.right = sub_child3

'''
                1
              /   \
            2      3
           /      / \
          4      5   6
'''
