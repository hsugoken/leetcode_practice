class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # Input
        # 0[[1,4,5,6]6 lower=0, upper=6 
        # Output
        #1,4 ->[1+1,4-1]=[2,3]
        # [[0,0],[2,3]]
        # Input
        # [[1,4,5,6] lower=0, upper=9
        #Output
        # [[0,0],[2,3],[7,9]]
        #diff>1
        #[0,0] [lower, nums[i]-1]
        #check lower, in between and end
        #[1,4,5,6] lower=0, upper=6
        #     ^ |
        #res = [[0,0],[2,3]]
        if len(nums)==0:
            return [[lower, upper]]
        res = []
        if lower<nums[0]:
            res.append([lower, nums[0]-1])
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i])>1:
                res.append([nums[i]+1, nums[i+1]-1])
        if upper>nums[-1]:
            res.append([nums[-1]+1, upper])
        
        return res