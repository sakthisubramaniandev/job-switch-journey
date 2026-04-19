# Problem: Reverse Linked List (LC 206)
# Difficulty: Easy
# Date: 18 April 2026
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Linked List — Three Pointers

# Key insight:
# Can only go FORWARD in linked list!
# Must reverse arrows while traversing
# CRITICAL: Save next_node BEFORE modifying current.next!

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next   # save next FIRST!
            current.next = prev        # reverse arrow
            prev = current             # move prev
            current = next_node        # move current

        return prev  # new head!


# Test
solution = Solution()
# Build: 1 → 2 → 3 → 4 → 5
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

result = solution.reverseList(n1)
while result:
    print(result.val, end=" → ")
    result = result.next
print("None")
# Output: 3 → 2 → 1 → None