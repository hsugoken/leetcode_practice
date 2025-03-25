class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        l = 0
        #abc 
        #abt
        for r in range(len(t)):
            if l<len(s) and s[l]==t[r]:
                l+=1
        return l==len(s)