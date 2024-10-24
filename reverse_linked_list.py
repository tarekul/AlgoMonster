class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    dummy = ListNode()

    current = head
    while current:
        next_node = current.next
        current.next = dummy.next
        dummy.next = current
        current = next_node
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print_linked_list(reverse_linked_list(node1))