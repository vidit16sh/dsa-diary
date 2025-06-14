"""
Question:
Leetcode 150 - Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (RPN).
Evaluate the expression and return the result as an integer.

Valid operators are '+', '-', '*', and '/'. Each operand may be an integer or another expression.
Note: Division between two integers should truncate toward zero.

---

Approach: Stack-Based Evaluation

- Initialize an empty stack.
- Iterate through the tokens:
  - If the token is a number, convert it to int and push to stack.
  - If it's an operator, pop two elements from the stack and apply the operation.
  - Push the result back onto the stack.
- At the end, the stack contains one element, the result.

Note: For division, use `int(float(b)/a)` to ensure truncation toward zero.

Time Complexity: O(n), where n is the number of tokens  
Space Complexity: O(n), for the stack used during evaluation

Test Case:
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: (2 + 1) * 3 = 9
"""

class Solution(object):
    def evalRPN(self, tokens):
        s = []  # Stack to hold operands

        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif i == '*':
                a, b = s.pop(), s.pop()
                s.append(a * b)
            elif i == '/':
                a, b = s.pop(), s.pop()
                s.append(int(float(b) / a))  # Ensure truncation toward 0
            else:
                s.append(int(i))  # Push operand to stack

        return s[0]

# ----------------------------------
# 🧪 Test Run Example
# ----------------------------------
# tokens = ["2", "1", "+", "3", "*"]
# sol = Solution()
# print(sol.evalRPN(tokens))  # Output: 9
