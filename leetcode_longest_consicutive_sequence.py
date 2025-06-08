# 🔶 Question:
# Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# ❗ Example:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    
    # ✅ Method 1: Sorting-based (O(n log n)) — Very fast in practice
    def longestConsecutiveSort(self, nums):
        if len(nums) == 0: 
            return 0 
        nums = list(set(nums))  # Remove duplicates
        nums.sort()             # Sort the list
        cnt = 1                 # Current sequence length
        max_len = 1             # Maximum found so far
        
        for i in range(len(nums) - 1):  
            if nums[i + 1] - nums[i] == 1:  
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        max_len = max(max_len, cnt)
        return max_len

    # ✅ Method 2: HashSet-based (O(n)) — Truly linear time
    def longestConsecutiveHashSet(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Only start if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest

# 🧪 Test Case
nums = [100, 4, 200, 1, 3, 2]

sol = Solution()
print("Using Sort:", sol.longestConsecutiveSort(nums))      # Output: 4
print("Using HashSet:", sol.longestConsecutiveHashSet(nums))  # Output: 4
