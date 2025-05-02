# Key Idea:
# Expand around every possible center (both odd and even).
# At each center, expand as long as the substring remains a palindrome.

# Edge Cases:
# 1. Empty string → return ""
# 2. All characters same → return entire string
# 3. No repeating characters → return any single character

# Time Complexity: O(N^2) — each center can expand up to O(N)
# Space Complexity: O(1) — constant extra space used (excluding result string)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Store the result substring and its length
        res = ""
        maxLen = float('-inf')

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check for odd-length palindromes (center at i)
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

            # Check for even-length palindromes (center between i and i+1)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

        
