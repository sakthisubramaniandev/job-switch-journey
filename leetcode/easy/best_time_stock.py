# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Date: 06 April 2026
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Greedy — track min price and max profit

# Key insight:
# Track minimum price seen so far
# Calculate profit at each step
# Track maximum profit seen so far
# Variables MUST be initialized outside the loop!

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


# Test cases
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(solution.maxProfit([7, 6, 4, 3, 1]))      # 0
print(solution.maxProfit([1, 2]))                # 1