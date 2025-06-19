"""
Question:
Leetcode 875 - Koko Eating Bananas

Koko loves to eat bananas. You are given an array `piles`, where each `piles[i]` represents the number of bananas in the i-th pile.
Koko can decide her eating speed `k` (bananas/hour). Each hour, she chooses a pile and eats `k` bananas from it. 
If the pile has less than `k` bananas, she eats all of them. The next hour, she can choose another pile.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

---

Approach: Binary Search on Answer

- The possible range for `k` is between `1` and `max(piles)` (since no need to eat faster than the biggest pile).
- Use binary search to minimize `k`:
    - For a given mid `k`, calculate the total time needed to eat all piles.
    - If total time is within `h`, `k` might be too big — try smaller.
    - If total time is over `h`, `k` is too small — try larger.
- Keep track of the valid minimum speed `res`.

Time Complexity: O(n log(max(piles)))
Space Complexity: O(1)

Test Case:
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: Minimum speed to eat all bananas in 8 hours is 4 bananas/hour.
"""

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        res = right  # Initialize result with upper bound

        while left <= right:
            k = (left + right) // 2
            totalTime = 0

            # Calculate time needed to eat all bananas at speed k
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            if totalTime <= h:
                res = k          # This speed works, try to minimize further
                right = k - 1
            else:
                left = k + 1     # Too slow, try higher speed

        return res
