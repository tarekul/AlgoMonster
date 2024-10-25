from collections import deque

def rotate_left_till_zero(nums):
    queue = deque(nums)
    while queue and queue[0] != 0:
        queue.append(queue.popleft())
    return list(queue)

print(rotate_left_till_zero([1, 2, 3, 4, 0, 5]))