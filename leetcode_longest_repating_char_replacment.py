"""
Question:
Leetcode 424 - Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any character in the string and
replace it with any uppercase English letter at most `k` times.

Return the length of the longest substring containing the same letter you can get after
performing at most `k` character replacements.

---

Approach:
- Use a sliding window technique.
- Maintain a frequency map `m` to count characters in the current window.
- Track `mf` (max frequency) — the count of the most frequent character in the window.
- If the number of characters that need to be replaced, i.e., `(window_size - mf)`, is more than `k`,
  shrink the window from the left.
- At each step, update the max window length `ln`.

Why it works:
- By always trying to expand the window and only shrinking when replacements exceed `k`,
  we ensure we explore the longest valid substring possible.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(1), since the alphabet size is constant (26 letters)

Test Case:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the second 'B' with 'A' to get "AABAAA" → length = 4
"""

from collections import defaultdict

def characterReplacement(s, k):
    m = defaultdict(int)  # character -> frequency
    l = 0
    ln = 0
    mf = 0  # most frequent character count in the current window

    for r in range(len(s)):
        m[s[r]] += 1
        mf = max(mf, m[s[r]])

        # If more than k characters need to be replaced, shrink the window
        if (r - l + 1) - mf > k:
            m[s[l]] -= 1
            l += 1

        ln = max(ln, r - l + 1)

    return ln

# ----------------------------
# 🧪 Test Run
# ----------------------------
s = "AABABBA"
k = 1
print("Longest Repeating Character Replacement Output:", characterReplacement(s, k))  # Output: 4
