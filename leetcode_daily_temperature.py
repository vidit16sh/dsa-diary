"""
Question:  
Leetcode 739 - Daily Temperatures

Given a list of daily temperatures `temperatures`, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is no future day 
for which this is possible, put `0` instead.

---

Approach: Monotonic Stack (Decreasing)

- Use a stack to store indices of unresolved days (temperatures waiting for a warmer day).
- Iterate through the temperature list:
  - While the current temperature is greater than the temperature at the top index in the stack:
    - Pop the index from the stack.
    - The difference between the current index and popped index is the number of days waited.
  - Push the current index onto the stack.

Why this works:
- The stack only keeps indices of temperatures in **decreasing order**.
- As soon as a warmer temperature is found, it resolves one or more past indices in the stack.

Time Complexity: O(n) — each index is pushed and popped at most once  
Space Complexity: O(n) — stack stores indices

Test Case:
Input: [73, 74, 75, 71, 69, 72, 76, 73]  
Output: [1, 1, 4, 2, 1, 1, 0, 0]
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)  # Result list initialized to 0s
        stack = []  # Monotonic stack to store indices

        for i in range(len(temperatures)):
            # Resolve previous days where today's temp is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pi = stack.pop()           # Previous index
                res[pi] = i - pi           # Days waited
            stack.append(i)                # Add current index to stack

        return res
