# 🔁 Problem: Reverse a Singly Linked List
# ----------------------------------------
# Given the head of a singly linked list, reverse the list and return the new head.
#
# ✅ Example:
# Input:  head = [1, 2, 3, 4, 5]
# Output:        [5, 4, 3, 2, 1]
#
# 🔍 Constraints:
# - The number of nodes in the list is in the range [0, 5000].
# - -5000 <= Node.val <= 5000
#
# 🧠 Goal: Reverse the list such that each node points to the previous node.

# ----------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ✅ Solution 1: Iterative Approach
# ----------------------------------------
# ⏱️ Time Complexity: O(n)
# 🗃️ Space Complexity: O(1)
class Solution(object):
    def reverseListIterative(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next   # store next node
            current.next = prev        # reverse the link
            prev = current             # move prev forward
            current = next_node        # move current forward
        
        return prev  # new head of the reversed list


# ✅ Solution 2: Recursive Approach
# ----------------------------------------
# ⏱️ Time Complexity: O(n)
# 🗃️ Space Complexity: O(n) due to call stack
class Solution(object):
    def reverseListRecursive(self, head, prev=None):
        if not head:
            return prev  # base case: return new head when reaching the end
        next_node = head.next
        head.next = prev
        return self.reverseListRecursive(next_node, head)
