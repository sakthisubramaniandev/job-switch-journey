# Problem: Middle of Linked List (LC 876)
# Difficulty: Easy
# Date: 19 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Fast and Slow Pointers

# Key insight:
# Fast moves 2x speed of slow
# When fast reaches end → slow is at middle!

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Test
# 1 → 2 → 3 → 4 → 5 → middle = 3
# 1 → 2 → 3 → 4 → middle = 3 (second middle)