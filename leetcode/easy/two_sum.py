# Problem: Two Sum
# Difficulty: Easy
# Date: 26 March 2026
# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: HashMap
# For each number, calculate complement = target - num
# Check if complement exists in HashMap
# If yes → return both indices
# If no → store current number in HashMap

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []


# Test cases
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(solution.twoSum([3, 2, 4], 6))         # [1, 2]
print(solution.twoSum([3, 3], 6))            # [0, 1]