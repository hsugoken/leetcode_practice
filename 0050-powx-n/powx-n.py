#-n can exceed the integer range thus to handle it n should be a 64-bit integer variable).
"""
Note: The standard multiplication algorithm for multiplying two numbers of d-digits each might take O(d^2) time, but most modern programming languages achieve a much lower time complexity i.e. O(d(logd)(loglogd)) by utilizing a divide-and-conquer strategy and leveraging fast fourier transforms. You can read more about the computational complexities of standard mathematical operations here
"""
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
#TC: O(log n)
#SC: O(1)
