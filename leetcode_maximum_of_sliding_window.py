"""
Question:
Leetcode 239 - Sliding Window Maximum

You are given an array `nums` and an integer `k`. There is a sliding window of size `k` that moves
from the very left of the array to the very right. You can only see `k` numbers in the window.
Each time the window moves right by one position.

Return the max value in each window.

---

Approach: Monotonic Deque

- Use a deque to store indices of useful elements in decreasing order of values.
- For each index `i`:
  - Remove the front element if it's outside the current window (`i - k`).
  - While the deque is not empty and the current element is greater than the last element's value,
    remove the last element (to maintain decreasing order).
  - Add the current index to the deque.
  - If `i >= k - 1`, the window is fully formed; append the front element's value (maximum) to result.

Why this works:
- The deque always stores indices in decreasing order of their values.
- The front of the deque is always the index of the current window's maximum.

Time Complexity: O(n) — each element is pushed and popped from the deque at most once  
Space Complexity: O(k) — for the deque and result array

Test Case:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [3,3,5,5,6,7]  
"""

from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()  # Will store indices of elements in decreasing order
    m = []       # Result array for maximums

    for i in range(len(nums)):
        # Remove indices that are out of this window
        if q and q[0] <= i - k:
            q.popleft()

        # Remove indices of all elements smaller than the current one
        while q and nums[i] > nums[q[-1]]:
            q.pop()

        # Add current index
        q.append(i)

        # Append the max (at the front of the deque) to result once the first window is complete
        if i >= k - 1:
            m.append(nums[q[0]])

    return m

# ----------------------------
# 🧪 Test Run
# ----------------------------
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print("Sliding Window Maximum Output:", maxSlidingWindow(nums, k))  # Output: [3,3,5,5,6,7]
