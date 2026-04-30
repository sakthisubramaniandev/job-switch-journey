# Problem: Merge Two Sorted Lists (LC 21)
# Difficulty: Easy
# Date: 30 April 2026
# Status: Accepted ✅
# Time Complexity: O(n+m)
# Space Complexity: O(1)
# Pattern: Dummy Node + Two Pointers

# Key insights:
# 1. Use dummy node — eliminates edge cases!
# 2. Assign NODE not value: current.next = list1
# 3. Move pointer: list1 = list1.next
# 4. current.next = list1 or list2 OUTSIDE loop!

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return dummy.next