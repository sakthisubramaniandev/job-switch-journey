# Problem: Search in a Binary Search Tree (LC 700)
# Difficulty: Easy
# Date: 29 April 2026
# Status: Accepted ✅
# Time Complexity: O(log n) average
# Space Complexity: O(h)
# Pattern: BST Property

# Key insight:
# val < root → go LEFT (val is smaller)
# val > root → go RIGHT (val is larger)
# val == root → return root (found!)

# Common mistake: confusing left/right direction!
# root.val < val → val is BIGGER → go RIGHT!

class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)