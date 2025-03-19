class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #|
        #1,1,1,0,0,1,0,0,0 
        #    ^
        
        #r=2
        #nums[r] = 1
        #l=0
        #max_len=3
        
        max_len = float('-inf')#
        l = 0
        for r in range(len(nums)):
            if nums[r]==0:
                k -= 1
            while k<0:
                if nums[l]==0:
                    k += 1
                l += 1
            #k=0
            max_len = max(max_len, r-l+1) 
        return max_len


        