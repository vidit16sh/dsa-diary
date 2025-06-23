"""
Question:
Leetcode 143 – Reorder List

You are given the head of a singly linked list.  
Reorder the list to follow the pattern:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Do not modify the values in the nodes, only the node connections may be changed.
Modify the list in-place.

---

🧠 Approach:

1. **Find the middle** of the linked list using the slow and fast pointer technique.
2. **Reverse** the second half of the list.
3. **Merge** the two halves, alternating nodes from the first and reversed second half.

---

Time Complexity: O(n)  
Space Complexity: O(1) — in-place modifications

Example:
Input: 1 → 2 → 3 → 4  
Output: 1 → 4 → 2 → 3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None — Do not return anything, modify head in-place instead.
        """

        if not head or not head.next or not head.next.next:
            return head

        # Step 1: Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Merge the two halves
        l1 = head       # First half
        l2 = prev       # Reversed second half

        while l2.next:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2

        return head  # Optional; function modifies list in-place
