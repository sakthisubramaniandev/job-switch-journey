# Problem: Palindrome Number
# Difficulty: Easy
# Date: 15 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Two Pointer

# Solved INDEPENDENTLY — applied two pointer
# immediately after learning the pattern! 🔥

# Approach: Convert to string, two pointer from both ends
class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] != number[right]:
                return False
            left += 1
            right -= 1

        return True


# One liner alternative
class SolutionOneLiner:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Test cases
solution = Solution()
print(solution.isPalindrome(121))   # True
print(solution.isPalindrome(-121))  # False
print(solution.isPalindrome(10))    # False
print(solution.isPalindrome(1221))  # True