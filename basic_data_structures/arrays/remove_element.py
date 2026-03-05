def remove_element(nums: list[int], target: int) -> list[int]:
    newArr = []
    
    for num in nums:
        if num != target:
            newArr.append(num)
    
    return newArr
    
if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = remove_element(nums, target)
    print(" ".join(map(str, res)))
    
"""
Remove Element
Write a function that removes all instances of a target value from an array, returning a new array without those elements.

For example:

[1, 2, 3, 2, 4, 2], target 2 → [1, 3, 4]
[5, 5, 5], target 5 → [] (empty array)
[1, 2, 3], target 7 → [1, 2, 3] (nothing removed)
Parameters:

nums: an array of integers
target: the value to remove
Return:

A new array with all instances of target removed
"""