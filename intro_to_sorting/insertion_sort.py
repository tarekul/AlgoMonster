def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

print(insertion_sort([5, 3, 1, 2, 4]))

# space_complexity = O(1)
# time_complexity = O(n^2)