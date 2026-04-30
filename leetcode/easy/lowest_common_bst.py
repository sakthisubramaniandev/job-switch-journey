# Problem: Lowest Common Ancestor of BST (LC 235)
# Difficulty: Easy
# Date: 29 April 2026
# Status: Accepted ✅
# Time Complexity: O(log n) average
# Space Complexity: O(h)
# Pattern: BST Property

# Key insight:
# Both p,q < root → LCA in left subtree
# Both p,q > root → LCA in right subtree
# Otherwise       → current root IS the LCA!

# Solved COMPLETELY INDEPENDENTLY! 🔥

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root