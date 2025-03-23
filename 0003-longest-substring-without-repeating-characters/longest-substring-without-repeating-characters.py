class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 #float('-inf')
        cur_window = set()
        l = 0
        # a b c b c b b
        #   ^
        for r in range(len(s)):
            while s[r] in cur_window:
                cur_window.remove(s[l])
                l += 1
            cur_window.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len



