# Problem: Same Tree (LC 100)
# Difficulty: Easy
# Date: 28 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(h)
# Pattern: Tree Recursion + AND condition

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)