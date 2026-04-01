# Problem: Valid Anagram
# Difficulty: Easy
# Date: 31 March 2026
# Time Complexity: O(n log n) — sort approach
# Space Complexity: O(1)

# Approach: Sort both strings and compare
# My instinct: check length → sort → compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# HashMap approach — O(n) time
class SolutionOptimal:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True


# Test cases
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))           # False
print(solution.isAnagram("car", "rac"))           # True