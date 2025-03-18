"""
Edge Cases: 
single character strings
all non-alphanumeric = "!!!"
m
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert all uppercase into lowercase letters.
        s = s.lower()
        #skip over empty strings
        left = 0
        right = len(s)-1
        while left<=right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True
#TC: O(N)
#SC: O(1)