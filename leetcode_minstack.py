"""
Question:
Leetcode 155 - Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `push(val)` — Pushes the element `val` onto the stack.
- `pop()` — Removes the element on the top of the stack.
- `top()` — Gets the top element.
- `getMin()` — Retrieves the minimum element in the stack.

---

Approach:
- Use a list `arr` where each element is a pair: [value, current_min]
- On `push`, store both the value and the minimum up to that point.
- On `pop`, just remove the top pair.
- On `top`, return the first value in the top pair.
- On `getMin`, return the second value in the top pair.

Time Complexity: O(1) for all operations  
Space Complexity: O(n) — extra space to store min alongside each value

Test Case:
Input: 
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.getMin()   ➞ -3
    obj.pop()
    obj.top()      ➞ 0
    obj.getMin()   ➞ -2
"""

class MinStack(object):

    def __init__(self):
        self.arr = []  # Each element is [value, current_min]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.arr:
            self.arr.append([val, val])
        else:
            current_min = min(val, self.arr[-1][1])
            self.arr.append([val, current_min])

    def pop(self):
        """
        :rtype: None
        """
        if self.arr:
            self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[-1][1]

# ----------------------------------
# 🧪 Test Run Example
# ----------------------------------
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())  # Output: -3
# obj.pop()
# print(obj.top())     # Output: 0
# print(obj.getMin())  # Output: -2
