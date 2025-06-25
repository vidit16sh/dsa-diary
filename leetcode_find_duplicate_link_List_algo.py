# ✅ Find the Duplicate Number (Floyd's Tortoise and Hare)
# Problem:
#   - Given an array of n + 1 integers where each number is in the range [1, n]
#   - Only one number is repeated (may appear multiple times)
#   - Do NOT modify the array, use only constant extra space

# 🔍 Key Insight:
#   - Treat nums as a linked list where each value points to an index
#   - A duplicate creates a cycle: finding the cycle's start gives the duplicate

# 🐢🐇 Floyd's Cycle Detection:
#   - Phase 1: Detect cycle by moving slow (1x) and fast (2x)
#   - Phase 2: Reset slow to start, move both 1 step until they meet again
#              → that meeting point is the duplicate number

def findDuplicate(nums):
    # Phase 1: Find intersection point in the cycle
    slow = fast = nums[0]
    while True:
        slow = nums[slow]          # Move by 1 step
        fast = nums[nums[fast]]    # Move by 2 steps
        if slow == fast:
            break                  # Cycle detected

    # Phase 2: Find entry point of the cycle = duplicate number
    slow = nums[0]                 # Reset slow to start
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow  # 🎯 duplicate number found
