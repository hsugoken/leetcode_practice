class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Can we have non-negative numbers? 
        #[1,2,-1,0,1,3] k=3
        #            ^
        # sum_seen = [1,3,2,2,3,6]
        # [1,2], [1,2,-1,0,1] [-1,0,1,3], [3]
        # [3]
        #  ^
        # sum_seen = [3]
        #
        csum_freq = {0:1}
        csum = 0
        res = 0
        for num in nums:
            csum += num
            res += csum_freq.get(csum-k, 0)
            csum_freq[csum] = csum_freq.get(csum, 0) + 1
        
        return res