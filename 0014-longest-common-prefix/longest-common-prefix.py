class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        res = ""
        # for i in range(len(strs)):
        #     for j in r
        # moringa 
        for i in range(len(word)):
            for w in strs:
                if not i<len(w) or w[i]!=word[i]:
                    return res
            res += word[i]
        return res
        

