# Problem: Balanced Binary Tree (LC 110)
# Difficulty: Easy
# Date: 27 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(h)
# Pattern: Tree Recursion + Signal (-1)

# Key insight:
# Return -1 as signal for unbalanced subtree
# -1 bubbles up to root
# If height(root) != -1 → balanced!

class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1


# Test cases
root1 = None  # empty tree → True
root2 = None  # build test trees as needed