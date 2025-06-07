# Question:
# Write an algorithm to determine if a number n is a "happy number".
# A happy number is a number defined by the following process:
# - Starting with any positive integer, replace the number by the sum of the squares of its digits.
# - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
# - Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example 1:
# Input: n = 19
# Output: True
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# Input: n = 20
# Output: False

class Solution(object):
    def isHappy(self, n): 
        dic = {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81} 
        def check_h(m):
            sum = 0 
            while m != 0:  
                sum = sum + dic.get(m % 10) 
                m = int(m/10)     
            return sum  
        n = check_h(n)
        x = set() 
        while n != 1:
            x.add(n)
            print(x)
            n = check_h(n) 
            if n in x: 
                return False 
        return True

sol  = Solution() 
print(sol.isHappy(20))  # Output: False
