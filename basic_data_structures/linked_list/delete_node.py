class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_node(head: Node, value: int) -> Node:
    if head is None:
        return None
    if head.val == value:
        return head.next
    head.next = delete_node(head.next, value)
    return head

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
    res = delete_node(head, value)
    print(" ".join(format_list(res)))
