class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0]**2+x[1]**2
        nums = [[dist(p), p] for p in points]
        def quickselect(l,r):
            if l>=r:
                return
            pivot = nums[r][0]
            p = l
            for i in range(l,r):
                if nums[i][0]<=pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]
            if p<k-1:
                quickselect(p+1, r)
            elif p>k-1:
                quickselect(l,p-1)
            else:
                return
        quickselect(0, len(nums)-1)
        return [p[1:][0] for p in nums[:k]]


        
        


