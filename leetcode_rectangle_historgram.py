"""
Question:
Leetcode 84 - Largest Rectangle in Histogram

Given an array of integers `heights` representing the heights of bars in a histogram, 
return the area of the largest rectangle that can be formed within the bounds of the histogram.

Each bar has width 1. You must return the area of the largest rectangle.

---

What is a Monotonic Increasing Stack?

A **monotonic increasing stack** is a stack in which the values (or indices referencing values) are maintained in strictly increasing order.  
In this problem, it’s used to:
- Track the indices of bars in the histogram.
- Ensure we always have increasing heights on the stack.
- When a smaller height is encountered, we pop from the stack and calculate areas using the popped bar as the smallest bar in a rectangle.
- This helps efficiently find the maximum possible rectangle at each step.

---

Approach:
- Iterate through each bar in `heights` and use a stack to track indices of increasing bars.
- For each bar, if it is **shorter than the bar at the top of the stack**, it means the rectangle with the top bar as the smallest can now be finalized.
- Pop from the stack and calculate the area using:
    - Height = height of the popped bar
    - Width = current index - index of the previous item in the stack - 1
- Do this until the stack is valid again, then push the current index.
- At the end, ensure all remaining bars in the stack are processed by extending the loop to `n + 1`.

Time Complexity: O(n)  
Space Complexity: O(n)

Test Case:
Input: heights = [3, 2, 10, 11, 5, 3]  
Output: 20  
Explanation: Largest rectangle is formed with height 5 and width 4 → area = 5 × 4 = 20
"""

heights = [3, 2, 10, 11, 5, 3]
n = len(heights)
m = 0  # Maximum area
stack = []  # Monotonic increasing stack

for i in range(n + 1):
    # Treat index n as a dummy height = 0 to flush stack at the end
    curr_height = 0 if i == n else heights[i]

    # Maintain increasing heights in the stack
    while stack and curr_height <= heights[stack[-1]]:
        h = heights[stack.pop()]  # Height of bar
        # Width between current index and the new top of stack
        w = i if not stack else i - stack[-1] - 1
        m = max(m, h * w)  # Update max area

    stack.append(i)  # Push current index

print("Largest Rectangle Area:", m)  # Output: 20
