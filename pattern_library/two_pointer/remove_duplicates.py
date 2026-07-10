"""
Given a sorted list of numbers with length at least 1, remove duplicates and return the new length. 
You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so that the first three elements become 0, 1, 2. Return 3 because the new length is 3.
"""

def remove_duplicates(arr: list[int]) -> int:
    if not arr:
        return 0
    
    insert_pos = 1
    
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[insert_pos] = arr[i]
            insert_pos += 1
    
    return insert_pos
        

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
    

