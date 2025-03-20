class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_window = {}
        count_t = {}
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        have = 0
        need = len(count_t)
        subs_len = float('inf')
        min_subs = [-1,-1]

        l = 0
        for i in range(len(s)):
            count_window[s[i]] = count_window.get(s[i], 0) + 1
            if s[i] in count_t and count_window[s[i]]==count_t[s[i]]:
                have +=1
            
            while have==need:
                if subs_len>(i-l+1):
                    subs_len = i-l+1
                    min_subs = [l,i]
                
                count_window[s[l]] -= 1
                if s[l] in count_t and count_window[s[l]]<count_t[s[l]]:
                    have -=1
                l +=1
        return s[min_subs[0]:min_subs[1]+1]