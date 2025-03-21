class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for x in range(len(s)):
            i=j=x
            while i>=0 and j<len(s) and s[i]==s[j]:
                count +=1
                i-=1
                j+=1
            i,j=x,x+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                count +=1
                i-=1
                j+=1
        return count


