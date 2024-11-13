"""
k workers need to read n newspapers. Each newspaper takes a certain amount of time to read. 
We want to minimize the maximum time any worker spends reading.

For example:
newspapers_read_times = [7,2,5,10,8], num_coworkers = 2

If we split the newspapers like this:
Worker 1: [7,2,5] = 14 time units
Worker 2: [10,8] = 18 time units
The maximum time spent is 18 units.

If we split them like this:
Worker 1: [7,2,5,8] = 22 time units  
Worker 2: [10] = 10 time units
The maximum time spent is 22 units.

The optimal split is:
Worker 1: [7,2,8] = 17 time units
Worker 2: [5,10] = 15 time units
Maximum time spent is 17 units.

We use binary search to find this optimal maximum time:
- The minimum possible time is max(newspapers_read_times) when each worker reads at most one paper
- The maximum possible time is sum(newspapers_read_times) when one worker reads all papers
- For each mid point, we check if it's feasible to split the work so no worker spends more than mid time
- If feasible, try a lower time. If not feasible, must use a higher time.
"""


from typing import List

def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    time, num_workers = 0, 1

    for read_time in newspapers_read_times:
        if read_time + time > limit:
            time = 0
            num_workers += 1
        time += read_time
    
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(newspapers_split([2,3,5,7], 3))
print(newspapers_split([7,2,5,10,8], 2))
print(newspapers_split([1,4,4], 3))
print(newspapers_split([15,15,15, 15], 4))