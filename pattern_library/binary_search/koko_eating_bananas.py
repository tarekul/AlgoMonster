"""
Imagine Koko the monkey has a few piles of bananas. The piles are represented by an array, like piles = [3, 6, 7, 11].
The zoo guards have left, and they will come back in exactly h = 8 hours.

Koko wants to eat all the bananas before they get back, but she likes to eat slowly. She wants to find the minimum speed k (bananas per hour) that allows her to eat every single pile within h hours.
(Note: If she finishes a pile in less than an hour, she rests for the remainder of that hour before starting the next pile).

Example 1:
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: At a speed of 4 bananas per hour, Koko can finish all piles in 8 hours.

Example 2:
Input: piles = [30, 11, 23, 4, 20], h = 5
Output: 30
Explanation: At a speed of 30 bananas per hour, Koko can finish all piles in 5 hours.

Example 3:
Input: piles = [30, 11, 23, 4, 20], h = 6
Output: 23
Explanation: At a speed of 23 bananas per hour, Koko can finish all piles in 6 hours.
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Return the minimum speed k that allows Koko to eat all piles within h hours.
        low, high = 1, max(piles) # The slowest Koko can eat is 1 banana per hour, the fastest is max(piles) bananas per hour
        
        while low <= high:
            mid = (low + high) // 2
            total_hours = 0
            for pile in piles:
                # Calculate hours needed for this pile at speed mid
                hours_needed = (pile + mid - 1) // mid  # Ceiling division
                total_hours += hours_needed
            
            if total_hours <= h:
                # Koko can finish all piles at this speed
                high = mid - 1
            else:
                # Koko needs to eat faster
                low = mid + 1
        
        return low
    
s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 8))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
