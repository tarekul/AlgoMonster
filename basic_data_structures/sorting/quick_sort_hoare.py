def quick_sort_hoare(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_hoare(arr, low, pivot - 1)
        quick_sort_hoare(arr, pivot, high)
        
    return arr

def partition(arr, low, high):
    pivot = arr[low + (high - low) // 2]
    print(f"\n--- New Partition | Range: {arr[low:high+1]} | Pivot: {pivot} ---")
    i = low
    j = high
    
    while i <= j:
        while arr[i] < pivot:
            i +=1
        while arr[j] > pivot:
            j -= 1
            
        if i <= j:
            print(f"Swapping {arr[i]} and {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Current List: {arr}")
            i += 1
            j -= 1
    
    return i
            
    

import unittest

class TestQuickSortHoare(unittest.TestCase):
    def testSort(self):
        nums = [38, 27, 43, 3, 9, 82, 10]
        quick_sort_hoare(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [3, 9, 10, 27, 38, 43, 82])
    def testSortSmallArray(self):
        nums = [5, 3, 2, 4, 1]
        quick_sort_hoare(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [1, 2, 3, 4, 5])
    
    
if __name__ == "__main__":
    unittest.main()