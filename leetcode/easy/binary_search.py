# Problem: Binary Search (LC 704)
# Difficulty: Easy
# Date: 17 April 2026
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search

# Key: Only works on SORTED arrays!
# Cut search space in half every step!

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Test cases
solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))   # 4
print(solution.search([-1,0,3,5,9,12], 2))   # -1
print(solution.search([5], 5))                # 0