class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i] (decision: take)
            subset.append(nums[i])
            dfs(i + 1)  # This recursive call was missing
            
            # don't include nums[i] (decision: don't take)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res