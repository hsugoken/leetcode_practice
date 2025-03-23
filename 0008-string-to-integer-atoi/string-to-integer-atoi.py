class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        i=0
        sign ="+"
        if s[i] in ["+","-"]:
            sign = s[i]
            i += 1
        s = s[i:]
        num_seen = False
        num = 0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            num = num*10 + int(s[i])
        num = num*(-1) if sign=="-" else num
        if num<-2**31:
            num = -2**31
        if num>2**31-1:
            num = 2**31-1

        return num
