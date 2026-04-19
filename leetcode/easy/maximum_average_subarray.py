# Problem: Maximum Average Subarray I
# Difficulty: Easy
# Date: 16 April 2026
# Status: Accepted ✅
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Sliding Window

# Key insight:
# Track maximum SUM during loop
# Divide by k ONCE at the end
# Key line: window_sum += arr[i] - arr[i-k]

class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


# Test cases
solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
print(solution.findMaxAverage([5], 1))                 # 5.0
print(solution.findMaxAverage([0,1,1,3,3], 4))        # 2.0