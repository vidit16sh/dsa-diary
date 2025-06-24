"""
Question:
Leetcode 138 – Copy List with Random Pointer

Each node in a linked list has:
- `next`: pointing to the next node
- `random`: pointing to any node in the list or `None`

You need to return a deep copy of the list.

---

🧠 Approach 1: Using a HashMap (Original → Copy Mapping)

Steps:
1. Traverse the list and create a mapping from each original node to its copy.
2. Set the `.next` and `.random` pointers in the copied nodes using this map.

Time Complexity: O(n)  
Space Complexity: O(n) for the hashmap

---

🧠 Approach 2: Optimized O(1) Space – Interleaving Trick

Steps:
1. **Clone and interleave nodes** in original list:  
   - For each node, insert its copy right after itself.
   - Original: A → B → C  
   - After interleaving: A → A' → B → B' → C → C'

2. **Set `.random` pointers**:  
   - For each original node `n`, do `n.next.random = n.random.next` (if `n.random` exists).

3. **Unweave the list**:  
   - Separate the original list and the copied list.

Time Complexity: O(n)  
Space Complexity: O(1)

"""

# --------------------------------------------
# Definition for a Node
# --------------------------------------------
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# --------------------------------------------
# Approach 1: Using HashMap (O(n) Space)
# --------------------------------------------
class Solution(object):
    def copyRandomList_hashmap(self, head):
        """
        :type head: Optional[Node]
        :rtype: Optional[Node]
        """
        if not head:
            return None

        mapping = {}  # Original node → Copied node
        current = head

        # First pass: clone all nodes
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next

        return mapping[head]


# --------------------------------------------
# Approach 2: Optimized O(1) Space – Interleaving Trick
# --------------------------------------------
    def copyRandomList(self, head):
        """
        Optimized O(1) space solution
        :type head: Optional[Node]
        :rtype: Optional[Node]
        """
        if not head:
            return None

        # Step 1: Interleave copied nodes with original nodes
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the two lists
        original = head
        copy = head.next
        copy_head = copy

        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head
