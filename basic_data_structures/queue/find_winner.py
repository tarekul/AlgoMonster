from collections import deque

def find_winner(n: int, k: int) -> int:
    queue = deque(range(n))
    
    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        queue.popleft()
    return queue.pop()

def find_winner2(n: int, k: int) -> int:
    if n == 1:
        return 0
    return (find_winner2(n - 1, k) + k) % n
            
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    res = find_winner(n, k)
    res2 = find_winner2(n, k)
    print(res)
    print(res2)

"""
Time Complexity: O(n * k) 
Space Complexity: O(n)
"""

"""
Is there a more efficient mathematical way to solve this problem? 

### Step 1: Define the Relationship

Let $J(n, k)$ be the index of the winner in a circle of $n$ people.

* **The Base Case:** In a circle of 1 person ($n=1$), the winner is always at **index 0**.
* **The Recursive Step:** $J(n, k) = (J(n-1, k) + k) \pmod n$.

### Step 2: The "Rewind" Logic (Mapping Back)

The reason this formula works is that it treats the winner of the smaller circle ($n-1$) as a "ghost" that we need to place back into the larger circle ($n$).

1. **Assume the Sub-problem is Solved:** We call `find_winner(n-1, k)`. This gives us the survivor's seat in a world where one person has already been kicked out.
2. **The Shift ($+k$):** In the original circle of $n$, the person at index $k-1$ was eliminated, and the "starting line" moved to the next person (index $k$). To find where our survivor was originally standing, we have to **add that $k$ back** to their current position.
3. **The Wrap-around ($\% n$):** Because it’s a circle, adding $k$ might result in a number higher than the available seats. The modulo by $n$ ensures the survivor lands on a valid original seat.

### Step 3: Example Walkthrough ($n=3, k=2$)

* **$n=1$:** Winner is at **0**.
* **$n=2$:** Take the winner from $n=1$ (0), shift by $k$ (2), and map to $n=2$ circle:

$$(0 + 2) \pmod 2 = \mathbf{0}$$


* **$n=3$:** Take the winner from $n=2$ (0), shift by $k$ (2), and map to $n=3$ circle:

$$(0 + 2) \pmod 3 = \mathbf{2}$$



**Final Winner:** Index 2.

Approach,Time Complexity,Why?
Queue/Simulation,O(n×k),"For every one of the n people, you have to perform k shifts in the queue."
Recursive/Mapping,O(n),You don't care how big k is; you just perform one math calculation per person.

"""




"""
Josephus Problem
The Josephus Problem is a classic elimination game. There are n people standing in a circle, numbered from 0 to n-1. Starting from person 0, you count k people around the circle. The kth person is eliminated and leaves the circle. Then, continue counting k people from the next person, and eliminate the kth person. This continues until only one person remains. Find the position (0-indexed) of the last remaining person.

Input
n: an integer representing the number of people in the circle (1 ≤ n ≤ 500)
k: an integer representing the elimination count (1 ≤ k ≤ n)
Output
An integer representing the 0-indexed position of the winner (the last person remaining)

Examples
Example 1:
Input: n = 5, k = 2

Output: 2

Explanation:

Circle: [0, 1, 2, 3, 4]
Count 2 from 0: eliminate person 1 → [0, 2, 3, 4]
Count 2 from 2: eliminate person 3 → [0, 2, 4]
Count 2 from 4: eliminate person 0 → [2, 4]
Count 2 from 2: eliminate person 4 → [2]
Winner: person 2
Example 2:
Input: n = 6, k = 3

Output: 0

Explanation:

Circle: [0, 1, 2, 3, 4, 5]
Eliminations: 2 → 5 → 3 → 1 → 4
Winner: person 0
Example 3:
Input: n = 1, k = 1

Output: 0

Explanation: Only one person, so they win automatically
"""