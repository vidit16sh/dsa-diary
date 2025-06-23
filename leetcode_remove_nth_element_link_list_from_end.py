"""
Question:
Leetcode 19 – Remove Nth Node From End of List

Given the head of a singly linked list, remove the n-th node from the end of the list 
and return its head.

---

🧠 Approach: Two-Pointer Technique (Fast & Slow Pointers)

1. Use a dummy node pointing to the head to simplify edge cases (e.g., removing the head itself).
2. Move the `right` pointer `n` steps ahead of the `left` pointer.
3. Then move both pointers one step at a time until `right` reaches the end.
4. Now `left` is just before the node to remove. Update `left.next` to skip the target node.

Why use a dummy?
- It simplifies handling the case where the head node itself needs to be removed.

Time Complexity: O(n) — traverse the list once  
Space Complexity: O(1) — constant extra space

Example:
Input: head = [1, 2, 3, 4, 5], n = 2  
Output: [1, 2, 3, 5]
"""

from collections import defaultdict

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # Step 1: Dummy node to handle edge cases smoothly
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 2: Move `right` pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Step 3: Move both pointers until `right` hits the end
        while right:
            left = left.next
            right = right.next

        # Step 4: Skip the node to be removed
        left.next = left.next.next

        return dummy.next
