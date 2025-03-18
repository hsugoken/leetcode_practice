#What variants of this are possible?
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #we will collect the frequency of all strings 
        #then we iterate through the order strings and add them to result
        #then we add rest of the strings
        char_freq = collections.defaultdict(int)
        for ch in s:
            char_freq[ch]+=1
        res_string = ""
        for ch in order:
            res_string += char_freq[ch]*ch
        
        for ch in s:
            if ch not in order:
                res_string += ch
        
        return res_string