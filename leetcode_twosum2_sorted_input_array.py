"""
Question:
Leetcode 167 - Two Sum II - Input array is sorted

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific `target` number. Return the indices of
the two numbers added by one (1-based indexing). You may assume that each input would have
exactly one solution and you may not use the same element twice.

Approach:
- Use the two-pointer technique.
- Initialize two pointers: `i` at the start and `r` at the end of the array.
- Calculate the sum of elements at those pointers:
  - If the sum equals the target, return the indices (+1 for 1-based).
  - If the sum is less than the target, move the left pointer (`i`) right.
  - If the sum is more than the target, move the right pointer (`r`) left.
- This works in O(n) time due to the sorted property of the array.

Test Case:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: The numbers at index 1 and 2 (2 + 7) add up to 9.
"""
class Solution(object):
    def twoSum(self, numbers, target):  
        i, r = 0, len(numbers) - 1 
        while i < r: 
            x = numbers[i] + numbers[r] 
            if x == target: 
                return [i + 1, r + 1] 
            elif x < target: 
                i += 1 
            else: 
                r -= 1 
