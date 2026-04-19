# Problem: Climbing Stairs
# Difficulty: Easy
# Date: 15 April 2026
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Dynamic Programming

# Key insight:
# ways(n) = ways(n-1) + ways(n-2)
# This IS the Fibonacci sequence!
# Store previous two values instead of recursing!

# My first attempt — recursion (correct but slow O(2^n))
class SolutionRecursive:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# Optimal — Dynamic Programming O(n)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


# Test cases
solution = Solution()
print(solution.climbStairs(1))   # 1
print(solution.climbStairs(2))   # 2
print(solution.climbStairs(3))   # 3
print(solution.climbStairs(4))   # 5
print(solution.climbStairs(5))   # 8