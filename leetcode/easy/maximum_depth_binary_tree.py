# Problem: Maximum Depth of Binary Tree (LC 104)
# Difficulty: Easy
# Date: 26 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(h)
# Pattern: Tree Recursion

# Tree Problem Template:
# 1. Base case — if not root return ???
# 2. Solve for left and right children
# 3. Combine results and return

# Key insight:
# depth = 1 (me) + max(left depth, right depth)
# Every node counts itself + picks deeper child!

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


# Test
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))  # 3