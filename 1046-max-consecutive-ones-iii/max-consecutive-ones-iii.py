class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #0,1,2,3,4,5,6,7,8
        #1,1,1,0,0,1,0,0,0 
        #l = 5
        #r = 8
        #k = 0
        #r-l+1 = 3
        #nums[l] = 1
        #nums[r=7] = 0
        #max_len= 6
        
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

#TC: O(N)
#SC: O(N)
        