# 🔀 Problem: Merge Two Sorted Linked Lists
# ----------------------------------------
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list and return the head of the new list.

# ✅ Example:
# Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

# ⏱️ Time Complexity: O(n + m), where n and m are lengths of list1 and list2
# 🗃️ Space Complexity: O(1), in-place merge using existing nodes

# ----------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to simplify appending
        dummy = temp = ListNode()
        
        # Merge nodes from both lists in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next  # Move the pointer forward

        # Append the remaining part of the non-empty list
        temp.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next
