# Problem: Contains Duplicate
# Difficulty: Easy
# Date: 03 April 2026
# Time Complexity: O(n)
# Space Complexity: O(n)

# Solved INDEPENDENTLY without hints! 🔥

# Approach 1 — HashMap (my solution)
class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count.get(num) >= 2:
                return True
        return False


# Approach 2 — Set (cleaner)
class SolutionSet:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# Test cases
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # True
print(solution.containsDuplicate([1, 2, 3, 4]))  # False
print(solution.containsDuplicate([1, 1, 1, 3]))  # True