def time_required_to_buy(tickets: list[int], k: int) -> int:
    time = 0
    target = tickets[k]
    
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], target)
        else:
            time += min(tickets[i], target - 1)
            
    return time

def time_required_to_buy_queue_v(tickets: list[int], k: int) -> int:
    indexes = list(range(len(tickets)))
    
    time = 0
    target = tickets[k]
    
    while target > 0:
        if tickets[indexes[0]] > 0:
            tickets[indexes[0]] -= 1
            time += 1
            if indexes[0] == k and tickets[indexes[0]] == 0:
                return time
            indexes.append(indexes.pop(0))
        else:
            indexes.pop(0)   

if __name__ == "__main__":
    tickets = [int(x) for x in input().split()]
    k = int(input())
    res = time_required_to_buy(tickets, k)
    res2 = time_required_to_buy_queue_v(tickets, k)
    print(res)
    print(res2)
    
    
"""
There are n people in a line to buy tickets. Each person wants to buy a certain number of tickets, represented by tickets[i]. The ticket counter sells one ticket at a time, and each person takes 1 second to buy one ticket. After buying a ticket, if a person still needs more tickets, they go to the back of the line.

You are the person at position k (0-indexed). Calculate how many seconds it takes for you to finish buying all your tickets.

Input
tickets: a list of integers where tickets[i] is the number of tickets person i wants to buy
k: an integer representing your position in line (0-indexed)
Output
An integer representing the total time in seconds for person k to finish buying all their tickets

Examples
####Example 1:

Input: tickets = [2, 3, 2], k = 2

Output: 6

Explanation:    

Time 1: Person 0 buys, queue = [3, 2, 1] -> [p1, p2, p0]
Time 2: Person 1 buys, queue = [2, 1, 2] -> [p2, p0, p1]
Time 3: Person 1 buys, queue = [1, 2, 1] -> [p0, p1, p2]
Time 4: Person 0 buys, queue = [2, 1, 0] -> [p1, p2, p0]
Time 5: Person 0 buys, queue = [1, 0, 1] -> [p2, p0, p1]
Time 6: Person 2 buys, queue = [0, 1, 0] -> [p0, p1, p2]

"""