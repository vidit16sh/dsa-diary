"""
Question:
Leetcode 567 - Permutation in String

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`,
or `False` otherwise.

In other words, return `True` if one of `s1`'s permutations is a substring of `s2`.

---

Approach: Sliding Window with Frequency Counting

- Use two frequency arrays (`h1` and `h2`) of size 26 to store character counts
  (assuming lowercase English letters).
- First, count the frequency of characters in `s1` and in the first `len(s1)` characters of `s2`.
- Then slide a window of size `len(s1)` across `s2`, updating the counts:
  - Increment the count of the new character entering the window.
  - Decrement the count of the character leaving the window.
- At each step, compare `h1` and `h2`. If equal, return `True`.

Time Complexity: O(n), where n = len(s2)
Space Complexity: O(1), since both arrays are of fixed size (26)

Test Case:
Input: s1 = "ab", s2 = "efabcd"
Output: True
Explanation: One permutation of "ab" is "ba", which is a substring of "efabcd".
"""

s1 = 'ab'
s2 = 'efabcd'

h1, h2 = [0] * 26, [0] * 26

# Initialize frequency maps for s1 and first window of s2
for i in range(len(s1)):
    h1[ord(s1[i]) - ord('a')] += 1
    h2[ord(s2[i]) - ord('a')] += 1

# Early check
if h1 == h2:
    print(True)

# Sliding window
l, r = 0, len(s1)
while r < len(s2):
    h2[ord(s2[r]) - ord('a')] += 1
    h2[ord(s2[l]) - ord('a')] -= 1
    l += 1
    r += 1
    if h1 == h2:
        print(True)
