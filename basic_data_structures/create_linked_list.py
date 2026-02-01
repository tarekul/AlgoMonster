class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: list[int]) -> Node:
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    
    return head

def format_list(node):
    if node is None:
        print("Reached end of list")
        return
    print(f"About to yield: {node.val}")
    yield str(node.val)
    print(f"Going to next node from: {node.val}")
    yield from format_list(node.next)
    
if __name__ == "__main__":
    values = [int(x) for x in input().split()]
    res = create_linked_list(values)
    print(" ".join(format_list(res)))