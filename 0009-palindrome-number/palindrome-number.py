class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        rev = 0
        while x>rev:
            #32
            #20+3
            rev = rev*10 + x%10
            x = x//10
        # When the length is an odd number, we can get rid of the middle digit 
        #by revertedNumber//10
        #For example when the input is 12321, at the end of the while loop we 
        #get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome
        #(it will always equal to itself), we can simply get rid of it.
        return rev==x or x==rev//10
