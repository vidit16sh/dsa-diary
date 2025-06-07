# Question:
# Given a string s of '(' , ')' and lowercase letters, 
# remove the minimum number of parentheses to make the input string valid.
# Return the resulting string.

# A string is valid if:
#  - Open brackets are closed by the same type of brackets.
#  - Open brackets are closed in the correct order.
#  - Every closing bracket has a corresponding open bracket before it.

# Example Test Cases:
# Input: s = "lee(t(c)o)de)"  => Output: "lee(t(c)o)de"
# Input: s = "a)b(c)d"        => Output: "ab(c)d"
# Input: s = "))(("           => Output: ""
# Input: s = "(a(b(c)d)"      => Output: "a(b(c)d)"

# Approach:
# 1. Traverse the string `s` left to right:
#    - Maintain a counter `cnt` for open parentheses '('.
#    - If '(' is found, increase `cnt`, and append to result list `r`.
#    - If ')' is found:
#        - If `cnt > 0`, append it to `r` and decrease `cnt`.
#        - Otherwise, it's an invalid ')' so skip it.
#    - If it's an alphabet character, append it to `r`.
# 2. Second pass: Remove unmatched '(' from the result by traversing it backwards.
#    - While `cnt > 0`, remove '(' from the end until all unmatched are gone.

class Solution(object):
    def minRemoveToMakeValid(self, s): 
        r = []   
        a = ['(',')','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
        cnt = 0 
        for x in s:  
            if x in a: 
                if x == '(': 
                    cnt += 1 
                    r.append(x) 
                elif x == ')' and cnt > 0: 
                    cnt -= 1 
                    r.append(x) 
                elif x.isalpha(): 
                    r.append(x) 
        for i in range(len(r)-1, -1, -1): 
            if cnt > 0: 
                if r[i] == '(': 
                    r.pop(i)  
                    cnt -= 1
        return ''.join(r)

# Sample usage:
sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
print(sol.minRemoveToMakeValid("a)b(c)d"))        # Output: "ab(c)d"
print(sol.minRemoveToMakeValid("))(("))           # Output: ""
print(sol.minRemoveToMakeValid("(a(b(c)d)"))      # Output: "a(b(c)d)"
