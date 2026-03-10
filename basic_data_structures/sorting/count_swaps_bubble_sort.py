def count_swaps_bubble_sort(arr: list[int]) -> int:
    n = len(arr)
    swaps = 0
    
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return swaps

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = count_swaps_bubble_sort(arr)
    print(res)


"""
Count the number of swaps needed to sort an array using bubble sort. This problem builds on your understanding of the bubble sort algorithm by tracking how many swap operations are performed.

Input
arr: a list of integers to be sorted
Output
An integer representing the total number of swaps performed during bubble sort

Examples
Example 1:
Input: arr = [1, 2, 3, 4, 5]

Output: 0

Explanation:

The array is already sorted, so no swaps are needed
Example 2:
Input: arr = [5, 4, 3, 2, 1]

Output: 10

Explanation:

This is the worst case (reverse sorted)
Pass 1: 4 swaps (5 bubbles to end)
Pass 2: 3 swaps (4 bubbles to position)
Pass 3: 2 swaps (3 bubbles to position)
Pass 4: 1 swap (2 bubbles to position)
Total: 4 + 3 + 2 + 1 = 10 swaps
"""