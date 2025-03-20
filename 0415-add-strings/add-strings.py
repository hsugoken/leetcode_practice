class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1)-1
        p2 = len(num2)-1
        res = []
        carry = 0
        while p1>=0 or p2>=0 or carry:
            if p1>=0:
                val1 = int(num1[p1])
            else:
                val1 = 0 
            if p2>=0:
                val2 = int(num2[p2])
            else:
                val2 = 0
            total = val1+val2+carry
            carry = total//10
            res.append(str(total%10)) 
            p1-=1
            p2-=1
        
        return ''.join(res[::-1])
