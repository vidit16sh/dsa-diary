# ✅ LeetCode 110. Balanced Binary Tree
# --------------------------
# ❓ Question:
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which:
#   - the left and right subtrees of **every node** differ in height by no more than 1.
#
# --------------------------
# 💡 Approach:
# Use a bottom-up DFS (post-order) to calculate height at each node.
# - If any subtree is unbalanced (height diff > 1), return -1 early.
# - Otherwise, return the height of the subtree as 1 + max(left, right).
# - If the final result is -1, the tree is unbalanced.
#
# 🔁 Time Complexity: O(n) — each node is visited only once.
# --------------------------
# 🧪 Test Case:
# Tree:
#       3
#      / \
#     9  20
#        / \
#       15  7
# ➤ isBalanced(root) ➞ True  ✅ (all nodes have balanced height)
#
# Tree:
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# ➤ isBalanced(root) ➞ False ❌ (left subtree is too tall)

def isBalanced(self, root):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if left == -1:
            return -1  # early exit if left subtree is unbalanced

        right = height(node.right)
        if right == -1:
            return -1  # early exit if right subtree is unbalanced

        if abs(left - right) > 1:
            return -1  # this node is unbalanced

        return 1 + max(left, right)

    return height(root) != -1
