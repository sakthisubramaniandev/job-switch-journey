def pallindromeWord(word):
    
    words = word.lower()
    left = 0
    right = len(words) - 1
    
    while left < right:
        if (words[left]) != (words[right]):
            return False
        left += 1
        right -= 1
    
    return True

print(pallindromeWord("racecar"))
print(pallindromeWord("hello"))
print(pallindromeWord("Madam"))