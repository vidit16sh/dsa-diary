"""
Question:
Leetcode 33 – Search in Rotated Sorted Array

You are given a rotated sorted array `nums` (with no duplicate values) and an integer `target`.
Search for the `target` and return its index. If it does not exist, return -1.

The array was originally sorted in ascending order but was rotated at some unknown pivot.
You must design an algorithm with O(log n) runtime complexity.

---

Approach:

1. **Step 1 – Find Pivot (Smallest Element Index)**:
   - Use binary search to locate the smallest element in the rotated array.
   - This gives us the index `pivot`, which splits the array into two sorted halves.

2. **Step 2 – Binary Search in Two Halves**:
   - Perform binary search in the left half (0 to pivot - 1) and right half (pivot to end).
   - Return the index if found in either half.
   - If not found in both → return -1.

Note: Recursive binary search is used in this solution.

Time Complexity: O(log n)  
Space Complexity: O(log n) due to recursion stack (can be O(1) if iterative search is used)

Test Case:
Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4  
Explanation: 0 is found at index 4
"""

class Solution(object):
    def search(self, nums, target):
        # Step 1: Find the index of the smallest element (pivot)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m  # Pivot is in the left half
            else:
                l = m + 1  # Pivot is in the right half

        pivot = l
        h = len(nums) - 1

        # Step 2: Standard recursive binary search
        def binary_search(nums, l, h, target):
            if l > h:
                return -1
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return binary_search(nums, m + 1, h, target)
            else:
                return binary_search(nums, l, m - 1, target)

        # Search in both halves
        left_result = binary_search(nums, 0, pivot - 1, target)
        right_result = binary_search(nums, pivot, h, target)

        # Return the index if found in any half
        if left_result == -1 and right_result == -1:
            return -1
        else:
            return max(left_result, right_result)
