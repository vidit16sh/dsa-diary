"""
Question:
Leetcode 3 - Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

Approach 1: Sliding Window with List (Less Efficient)
- Use a list `t` to store characters in the current substring.
- For each character `s[r]`:
  - If `s[r]` is already in `t`, pop from the front until it's removed.
  - Append the character and update the maximum length.
- Time Complexity: O(n^2) due to list popping from front.
- Space Complexity: O(n)

Approach 2: Optimized Sliding Window with HashMap
- Use a dictionary `m` to store the last seen index of characters.
- Use two pointers `l` and `r` to define the window.
- If `s[r]` is in the map and its index is within the current window,
  move `l` to `m[s[r]] + 1` to skip duplicates.
- Update the map and compute window length.
- Time Complexity: O(n)
- Space Complexity: O(n)

Test Case:
Input: s = "abba"
Expected Output: 2 (either "ab" or "ba")
"""

def longest_substring_list(s):
    r = 0
    cnt = 0
    t = []

    while r < len(s):
        while s[r] in t:
            t.pop(0)
        t.append(s[r])
        cnt = max(cnt, len(t))
        r += 1

    return cnt

def longest_substring_map(s):
    l = 0
    m = {}  # char -> last index
    n = 0   # max length

    for r in range(len(s)):
        if s[r] in m and m[s[r]] >= l:
            l = m[s[r]] + 1
        m[s[r]] = r
        n = max(n, r - l + 1)

    return n

# ----------------------------
# 🧪 Test Run
# ----------------------------
s = "abba"
print("Approach 1 (List-based) Output:", longest_substring_list(s))  # Output: 2
print("Approach 2 (Map-based) Output:", longest_substring_map(s))    # Output: 2
