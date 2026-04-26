# Problem: Valid Parentheses (LC 20)
# Difficulty: Easy
# Date: April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Stack

# Key insight:
# Opening bracket → push to stack
# Closing bracket → check top of stack matches
# End → stack must be empty!

# Two failure cases:
# 1. Stack empty when closing bracket found
# 2. Top of stack doesn't match closing bracket

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


# Test cases
solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([)]"))    # False
print(solution.isValid("{[]}"))    # True