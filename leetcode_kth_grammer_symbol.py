"""
Question:
Leetcode 779 - K-th Symbol in Grammar

On the first row, we write a 0. 
Now in every subsequent row, we replace 0 with "01", and 1 with "10".

Given two integers n and k:
- Return the k-th (1-indexed) symbol in the n-th row of this grammar sequence.

---

Approach: Recursion

- Observe how the pattern evolves:
    Row 1: 0  
    Row 2: 0 1  
    Row 3: 0 1 1 0  
    Row 4: 0 1 1 0 1 0 0 1  
    ...
- Each symbol spawns two children:  
    - 0 → 01  
    - 1 → 10

- Recursive Insight:
    - The first half of row `n` is the same as row `n-1`
    - The second half is the inverse (flip) of row `n-1`
    - So:
        - If `k <= mid`, recurse on left half: `rn(n-1, k)`
        - Else, recurse on right half and flip the result: `1 - rn(n-1, k - mid)`

Time Complexity: O(n) — because we go down at most `n` levels in recursion  
Space Complexity: O(n) — recursion stack

Test Case:
Input: n = 2, k = 2  
Output: 1  
Explanation: Row 2 is [0, 1], so the 2nd symbol is 1
"""

def rn(n, k):
    print("n =", n, ", k =", k)  # Debug print to trace recursion

    # Base case: first symbol is 0
    if n == 1 and k == 1:
        return 0

    mid = (2 ** (n - 1)) // 2

    if k <= mid:
        return rn(n - 1, k)
    else:
        return 1 - rn(n - 1, k - mid)

# ----------------------------
# 🧪 Test Run
# ----------------------------
print("Result:", rn(2, 2))  # Output: 1
