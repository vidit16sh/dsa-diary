"""
Question:
Leetcode 153 – Find Minimum in Rotated Sorted Array  

You are given an integer array `nums` sorted in ascending order (with **no duplicates**),
but the array may have been **rotated** at an unknown pivot.  
Return the minimum element of this array.

---

Two Approaches Implemented Below
--------------------------------

1. **Linear Scan (Early‑Exit) – O(n) Time, O(1) Space**
   • Walk forward with two pointers `l` and `r` while the sequence is still strictly
     increasing (`nums[l] < nums[r]`).  
   • If we reach the end, the array was never rotated → `nums[0]` is the minimum.  
   • Otherwise, once the increasing trend breaks, `nums[r]` is the first element
     smaller than its predecessor, hence the minimum.

2. **Binary Search (Optimised) – O(log n) Time, O(1) Space**
   • Classic binary search on a rotated sorted array:  
     – Maintain `[l, r]` window.  
     – Compute `m = (l + r) // 2`.  
     – If `nums[m] < nums[r]`, the minimum lies in the **left half** (including `m`).  
        Set `r = m`.  
     – Else the minimum lies in the **right half** (excluding `m`).  
        Set `l = m + 1`.  
   • Loop until `l == r`; `nums[l]` (or `nums[r]`) is the minimum.

Both functions accept a *rotated sorted array without duplicates* and return the minimum.
"""

from typing import List

# ---------- Approach 1 : Linear Scan -----------------------------------------
def findMin_linear(nums: List[int]) -> int:
    """
    O(n) linear‑scan solution.
    """
    l, r = 0, 1
    # Walk while strictly increasing
    while r < len(nums) and nums[l] < nums[r]:
        l += 1
        r += 1

    # If we reached the end, array wasn't rotated
    if r == len(nums):
        return nums[0]
    # First drop found → nums[r] is minimum
    return nums[r]


# ---------- Approach 2 : Binary Search ---------------------------------------
def findMin_binary(nums: List[int]) -> int:
    """
    O(log n) binary‑search solution.
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] < nums[r]:
            r = m          # Minimum is at m or to its left
        else:
            l = m + 1      # Minimum is to the right of m
    return nums[l]


# ---------------------------- 🧪 Test Run ------------------------------------
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print("Linear  min:", findMin_linear(nums))   # ➞ 0
    print("Binary  min:", findMin_binary(nums))   # ➞ 0
