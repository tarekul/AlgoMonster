class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert_at_head(head: Node, value: int) -> Node:
    new_node = Node(value)
    new_node.next = head
    return new_node

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    value = int(input())
    res = insert_at_head(head, value)
    print(" ".join(format_list(res)))
