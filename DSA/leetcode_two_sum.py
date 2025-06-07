# Problem: Two Sum
# Given an array of integers `nums` and an integer `target`, return the indices 
# of the two numbers such that they add up to the target.
#
# Assumptions:
# - Each input has exactly one solution.
# - You may not use the same element twice.
# - You can return the answer in any order.
#
# Example:
# Input: nums = [2, 11, 7, 5], target = 9
# Output: [0, 2]
# Explanation: nums[0] + nums[2] = 2 + 7 = 9
#
# Approach:
# - Use a dictionary `seen_nums` to store numbers we've already seen along with their indices.
# - For each number `n` in the list:
#     - Check if the complement (`target - n`) is already in the dictionary.
#     - If yes, return the indices.
#     - If not, store the current number and its index in the dictionary.
# - This makes the solution O(n) time complexity.

def two_sum(nums, target):
    seen_nums = {}
    for i, n in enumerate(nums):  # Iterates both index and element
        if target - n in seen_nums:
            return [seen_nums[target - n], i] 
        seen_nums[n] = i

# Test case
nums = [2, 11, 7, 5]
target = 9
print(two_sum(nums, target))  # Output: [0, 2]
