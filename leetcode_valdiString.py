# ✅ Question: Valid Parentheses
# Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.
#
# Example test cases:
#   Input: "()"       → Output: True
#   Input: "()[]{}"   → Output: True
#   Input: "(]"       → Output: False
#   Input: "([)]"     → Output: False
#   Input: "{[]}"     → Output: True

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif stack and dic[stack.pop()] == i:
                continue
            else:
                return False
        return not stack

# Example test case
sol = Solution()
print(sol.isValid("()"))  # Output: True
