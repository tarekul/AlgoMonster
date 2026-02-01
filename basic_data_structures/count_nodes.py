class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def count_nodes(head: Node) -> int:
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    res = count_nodes(head)
    print(res)
