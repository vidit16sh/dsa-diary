"""
Question:
Leetcode 76 - Minimum Window Substring

Given two strings `s` and `t`, return the minimum window in `s` which will contain all the characters in `t`.
If there is no such window in `s` that covers all characters in `t`, return an empty string `""`.

---

Approach: Sliding Window + Hash Maps

- Use two dictionaries:
  - `h1` to store frequency of each character in `t`
  - `h2` to store frequency of characters in the current window of `s`
- Expand the right pointer `r` across `s` and update `h2`.
- For every character `c` in `t`, when `h2[c]` matches `h1[c]`, we increment `e2`.
- When all required characters are matched (`e1 == e2`), try to shrink the window from the left (`l`) while still valid.
- Keep track of the minimum window size and its start/end positions.

Time Complexity: O(n), where n is the length of `s`  
Space Complexity: O(1), since character set is fixed (only ASCII letters)

Test Case:
Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"  
Explanation: The minimum window substring that contains A, B, and C is "BANC".
"""

def minWindow(s, t):
    if len(s) < len(t) or not t:
        return ""

    h1, h2 = {}, {}
    m = len(s) + 1
    start = end = 0

    # Count frequency of characters in t
    for c in t:
        h1[c] = 1 + h1.get(c, 0)

    e1 = len(h1)  # total unique chars in t
    e2 = 0        # matched unique chars in current window
    l = 0

    for r in range(len(s)):
        h2[s[r]] = 1 + h2.get(s[r], 0)

        # Count this character as matched if it satisfies required count
        if s[r] in h1 and h2[s[r]] == h1[s[r]]:
            e2 += 1

        # Try to contract window while valid
        while e1 == e2:
            if (r - l + 1) < m:
                m = r - l + 1
                start, end = l, r

            if s[l] in h1 and h2[s[l]] == h1[s[l]]:
                e2 -= 1
            h2[s[l]] -= 1
            l += 1

    return s[start:end + 1] if m != len(s) + 1 else ""

# ----------------------------
# 🧪 Test Run
# ----------------------------
s = "ADOBECODEBANC"
t = "ABC"
print("Minimum Window Substring Output:", minWindow(s, t))  # Output: "BANC"
