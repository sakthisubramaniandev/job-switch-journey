# Problem: Symmetric Tree (LC 101)
# Difficulty: Easy
# Date: 28 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(h)
# Pattern: Tree Recursion + Mirror comparison

# Key insight:
# left.left must mirror right.right
# left.right must mirror right.left
# Cross comparison — not same side!

# Bug fixed: nested functions don't use self!

class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and \
                   isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)

        return isMirror(root.left, root.right)