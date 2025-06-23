"""
Question:
Leetcode 141 – Linked List Cycle

Given the head of a linked list, determine if the linked list has a cycle in it.

A cycle occurs when a node's next pointer points to a previously visited node.
Return True if there is a cycle in the linked list; otherwise, return False.

---

🧠 Approach 1: Using a Hash Set (Visited Nodes)
- Use a hash set to store all visited nodes.
- If a node is already in the set when visited again, there is a cycle.
- Otherwise, continue traversing.

Time Complexity: O(n)  
Space Complexity: O(n)

---

🧠 Approach 2: Floyd’s Cycle Detection (Tortoise and Hare)
- Use two pointers: `slow` moves one step at a time, `fast` moves two steps.
- If a cycle exists, `slow` and `fast` will eventually meet inside the loop.
- If `fast` reaches the end (`None`), there’s no cycle.

Time Complexity: O(n)  
Space Complexity: O(1)

"""

from collections import defaultdict

class Solution(object):
    def hasCycle_hashset(self, head):
        """
        Detect cycle using a hash set.
        :type head: ListNode
        :rtype: bool
        """
        visited = defaultdict(set)
        while head:
            if visited[head]:
                return True
            visited[head] = 1
            head = head.next
        return False

    def hasCycle_floyd(self, head):
        """
        Detect cycle using Floyd's cycle detection algorithm.
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next  # Create cycle

# sol = Solution()
# print(sol.hasCycle_hashset(head))  # ➞ True
# print(sol.hasCycle_floyd(head))    # ➞ True
