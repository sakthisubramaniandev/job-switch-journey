# Problem: Linked List Cycle (LC 141)
# Difficulty: Easy
# Date: 19 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Fast and Slow Pointers (Floyd's Algorithm)

# Key insight:
# No cycle → fast reaches None
# Cycle exists → fast catches slow → they meet!

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False