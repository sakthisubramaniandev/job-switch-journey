# Problem: Diameter of Binary Tree (LC 543)
# Difficulty: Easy
# Date: 27 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(h)
# Pattern: Tree Recursion + Global Variable

# Key insight:
# At each node: diameter = left_height + right_height
# Track GLOBALLY — diameter may not pass through root!
# self.diameter persists across all recursive calls!

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        height(root)
        return self.diameter