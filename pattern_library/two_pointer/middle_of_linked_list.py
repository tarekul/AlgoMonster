"""
Middle of a Linked List
Find the middle node of a linked list.

Input: 0 1 2 3 4

Output: 2

If the number of nodes is even, then return the second middle node.

Input: 0 1 2 3 4 5

Output: 3
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    if head.next == None:
        return head
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val
    

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
