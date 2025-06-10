"""
Question:
Leetcode 42 - Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Approach (Two-Pointer Technique):
- Initialize two pointers `l` and `r` at the start and end of the height array.
- Track `leftMax` and `rightMax` to store the maximum heights seen so far from both ends.
- At each step, compare `leftMax` and `rightMax`:
  - If `leftMax` is smaller:
    - Move `l` to the right.
    - If the current height is less than `leftMax`, water can be trapped: add the difference.
  - Else:
    - Move `r` to the left.
    - If the current height is less than `rightMax`, water can be trapped: add the difference.
- Continue until the two pointers meet.

Why it works:
- Water trapped depends on the shorter of the tallest bars on either side.
- We accumulate the difference between the current height and the boundary maximum.

Time Complexity: O(n)
Space Complexity: O(1)

Test Case:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: Trapped water forms between the elevations. Total trapped units = 6.
"""

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
l, r = 0, len(height) - 1
leftMax, rightMax = height[l], height[r]
s = 0  # Total trapped water

while l < r:
    if leftMax < rightMax:
        l += 1
        leftMax = max(leftMax, height[l])
        s += leftMax - height[l]  # Water trapped at position l
    else:
        r -= 1
        rightMax = max(rightMax, height[r])
        s += rightMax - height[r]  # Water trapped at position r

print(s)  # Expected Output: 6
