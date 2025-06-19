"""
Question:
Leetcode 74 - Search a 2D Matrix

You are given an `m x n` integer matrix where each row is sorted in ascending order,
and the first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return True if `target` is in the matrix, and False otherwise.

---

Approach: Binary Search Over a Virtual 1D Array

- Treat the 2D matrix as a flattened sorted 1D array of size `rows * cols`.
- Use binary search:
    - Calculate the middle index `mid` between `low` and `high`.
    - Convert `mid` back to 2D coordinates using:  
      `r = mid // cols` (row), `c = mid % cols` (column)
    - Compare `matrix[r][c]` with the `target`:
        - If equal → return True
        - If less than target → search right half
        - If greater → search left half

Time Complexity: O(log(m * n))  
Space Complexity: O(1)

Test Case:
Input:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
Output: True
Explanation: 3 is located at position (0,1)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            r, c = mid // cols, mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

# ----------------------------------
# 🧪 Test Run Example
# ----------------------------------
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# target = 3
# sol = Solution()
# print(sol.searchMatrix(matrix, target))  # Output: True
