"""
Question:  
Leetcode 22 - Generate Parentheses

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

Approach: Backtracking with a Stack

- Use a recursive function `dp` to build the result string step-by-step.
- Maintain a stack to store the current combination of parentheses.
- Use two counters:
  - `op` → number of open brackets used so far
  - `cl` → number of close brackets used so far

Recursive Logic:
1. If `cl < op`, it means we can add a closing bracket `)` (to match a previously opened one).
2. If `op < n`, it means we can still add an opening bracket `(`.
3. If both `op == cl == n`, we have a valid combination → append it to the result.
4. After every recursive call, we pop from the stack to backtrack and try other possibilities.

Why `stack.pop()` is needed:
- It undoes the last step after a recursive call.
- This allows us to try the next possible path without affecting other branches of recursion.

Time Complexity: O(2^n) — in the worst case, we explore every possible combination  
Space Complexity: O(n) — for the recursion call stack and current string

Test Case:
Input: n = 3  
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
"""

class Solution(object):
    def generateParenthesis(self, n): 
        op, cl = 0, 0                 # op: open count, cl: close count
        stack = []                    # current combination being built
        result = []                   # final list of valid combinations

        def dp(stack, op, cl): 
            if cl < op:              # add close only if it's valid
                stack.append(")") 
                dp(stack, op, cl + 1) 
                stack.pop()          # backtrack after recursion

            if op < n:               # add open if we still can
                stack.append("(") 
                dp(stack, op + 1, cl) 
                stack.pop()          # backtrack after recursion

            elif op == cl == n:      # if valid combo, add to result
                result.append(''.join(stack)) 
                return

        dp(stack, op, cl) 
        return result
