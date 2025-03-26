"""
Q: "How would you handle decimal points or scientific notation?"
Answer: For decimal points, stop at the decimal (e.g., "3.14" → 3). For scientific notation, you'd need to parse the mantissa and exponent separately.

Q: "How would you implement this without using built-in functions like isdigit()?"
Answer: Check if character is between '0' and '9': '0' <= c <= '9'
"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #convert string to 32-bit signed integer
        #ignore leading whitespace
        s = s.lstrip()
        #"-123x1 adasd"
        #     ^
        #num = 123
        #sign = -1
        if not s:
            return 0
        #check for sign
        i = 0
        
        sign = "+"
        if s[i] in ["+", "-"]:
            sign = s[i]
            i+=1
        #read until you get a non-digit character
        num = 0
        while i<len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        num = num*(-1) if sign=="-" else num
        #rounding
        if num<-2**31:
            num = -2**31
        if num>2**31-1:
            num = 2**31 - 1
        
        return num