def quick_sort_lomuto(arr, low, high):
  if low < high:
    p_idx = partition(arr, low, high)
  
    quick_sort_lomuto(arr, low, p_idx - 1)
    quick_sort_lomuto(arr, p_idx + 1, high)
  
  return arr
  
def partition(arr, low, high):
  p = arr[high]
  j = low - 1
  
  for i in range(low, high):
    if arr[i] <= p:
      j += 1
      arr[i], arr[j] = arr[j], arr[i]
      
  arr[j + 1], arr[high] = arr[high], arr[j + 1]
  
  return j + 1
      
    
import unittest

class TestQuickSortLomuto(unittest.TestCase):
    def testSort(self):
        nums = [38, 27, 43, 3, 9, 82, 10]
        quick_sort_lomuto(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [3, 9, 10, 27, 38, 43, 82])
    def testOneElement(self):
        nums = [1]
        quick_sort_lomuto(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [1])
        

if __name__ == "__main__":
    unittest.main()