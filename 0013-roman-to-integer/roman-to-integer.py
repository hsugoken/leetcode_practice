class Solution:
    def romanToInt(self, s: str) -> int:
        #largest to smallers: add them up
        #smaller before larger: substract smaller
        roman = {
                "I":1, "V":5, "X":10, "L":50, "C":100,
                 "D":500, "M":1000 
                 }
        res = 0

        for i in range(len(s)):
            #first we check if we are going to substract this value
            #first check if we have a character that comes after this
            #and if then is it inbounds and then we check the value
            if (i+1)<len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res