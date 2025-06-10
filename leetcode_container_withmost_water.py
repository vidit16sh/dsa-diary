"""
Question:
Leetcode 11 - Container With Most Water

You are given an integer array `height` of length n. There are n vertical lines drawn such that
the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container such that the container contains
the most water. Return the maximum amount of water a container can store.

Note: You may not slant the container.

Approach:
- Use the two-pointer technique.
- Start with one pointer at the beginning (left) and one at the end (right).
- Calculate the area between the two lines: `min(height[l], height[r]) * (r - l)`
- Move the pointer pointing to the shorter line inward (as that may help increase the area).
- Continue until both pointers meet.

Why it works:
- Moving the shorter height has the potential to increase the height in the next comparison.
- The wider width is only reduced when we move pointers, so we maximize height to compensate.

Time Complexity: O(n)
Space Complexity: O(1)

Test Case:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The max area is formed between heights 8 and 7 with distance 7 - 1 = 7 → 7 * 7 = 49
"""

class Solution(object):
    def maxArea(self, height): 
        m = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Calculate area and update maximum
            m = max(m, min(height[l], height[r]) * (r - l))

            # Move the shorter line inward
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return m


# ----------------------------
# 🧪 Test Case
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))  # Expected Output: 49
