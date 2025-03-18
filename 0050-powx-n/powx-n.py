class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        res = 1
        while n>0:
            if n%2==1:
                res = res*x
            x = x**2
            n=n//2
        return res
