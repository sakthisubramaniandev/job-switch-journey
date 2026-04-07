# Problem: Maximum Subarray
# Difficulty: Easy
# Date: 07 April 2026
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Kadane's Algorithm

# Core idea:
# At each position decide:
# extend current subarray OR start fresh?
# Pick whichever gives LARGER sum!

# Key line:
# current = max(num, current + num)
#                ↑         ↑
#           start fresh   extend

class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum


# Test cases
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(solution.maxSubArray([1]))                       # 1
print(solution.maxSubArray([5,4,-1,7,8]))              # 23
print(solution.maxSubArray([1,-2,3,6,-1]))             # 9