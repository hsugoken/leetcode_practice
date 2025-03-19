class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #          |
        #1,1,1,0,0,1,0,0,0 
        #              ^
        #l=5
        #r=8
        #k=0
        #nums[r] = 0
        #max_len=6
        
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
            max_len = max(max_len, r-l+1)  #4<6
        return max_len


        