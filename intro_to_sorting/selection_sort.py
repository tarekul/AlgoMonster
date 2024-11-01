def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 3, 1, 2, 4]))

# space_complexity = O(1)
# time_complexity = O(n^2)

"""
This is an unstable algorithm because an earlier element may be moved behind a later equal element.
Example: [2 of Diamonds, 5 of Hearts, 3 of Clubs, 5 of Spades, 2 of Hearts]
[2 of Diamonds, 2 of Hearts, 3 of Clubs, 5 of Spades, 5 of Hearts]
Notice that we swap the 5 of Hearts with 2 of Hearts and 5 of Hearts ends up behind 5 of spades.

This is an in-place algorithm because it sorts the array in place and does not require additional memory for another array.
"""