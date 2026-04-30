# Problem: Intersection of Two Linked Lists (LC 160)
# Difficulty: Easy
# Date: 30 April 2026
# Status: Accepted ✅
# Time Complexity: O(n+m)
# Space Complexity: O(1)
# Pattern: Redirect Pointer Trick

# Key insight:
# Redirect p1 to headB when exhausted
# Redirect p2 to headA when exhausted
# Both travel len(A)+len(B) — meet at intersection!
# No intersection → both become None together!

class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1