# Problem: Search Insert Position (LC 35)
# Difficulty: Easy
# Date: 17 April 2026
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search variant

# Key insight:
# Same as binary search but return LEFT when not found
# left pointer = correct insertion position!

class Solution:
    def searchInsert(self, nums, target):
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

        return left  # insertion position!


# Test cases
solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))  # 2
print(solution.searchInsert([1,3,5,6], 2))  # 1
print(solution.searchInsert([1,3,5,6], 7))  # 4
print(solution.searchInsert([1,3,5,6], 0))  # 0