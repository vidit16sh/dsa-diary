"""
Question:
Leetcode 15 - 3Sum

Given an integer array `nums`, return all the triplets [nums[i], nums[j], nums[k]] such that:
- i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0
- The solution set must not contain duplicate triplets.

Approach (Efficient Version):
- Sort the array.
- Iterate through the array and fix one element `a = nums[i]`.
- Use two pointers (`j`, `k`) to find two other elements such that a + nums[j] + nums[k] == 0.
- Skip duplicates for the fixed element and the two-pointer elements.
- If the current fixed number is greater than 0, break early (since the array is sorted).
- Time Complexity: O(n^2)
- Space Complexity: O(1) excluding the output.

Approach (Inefficient Version):
- Also uses the two-pointer technique but lacks proper elif/else branching.
- After finding a valid triplet, it still evaluates the next conditions.
- This causes redundant pointer moves and unnecessary checks.
- Slightly more error-prone and less optimal than the efficient version.

Test Case:
Input: nums = [-1, 0, 1, 2, -1, -4]
Expected Output: [[-1, -1, 2], [-1, 0, 1]]
"""

class Solution(object):
    
    def threeSum_efficient(self, nums):
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                x = val + nums[j] + nums[k]
                if x == 0:
                    res.append([val, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif x < 0:
                    j += 1
                else:
                    k -= 1
        return res

    def threeSum_inefficient(self, nums):
        l = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if x == 0:
                    l.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                if x < 0:
                    j += 1
                else:
                    k -= 1
        return l


# ----------------------------
# 🧪 Test Case
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    print("Efficient Version Output:")
    print(sol.threeSum_efficient(nums))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

    print("\nInefficient Version Output:")
    print(sol.threeSum_inefficient(nums))  # Should return the same result but may do more work
