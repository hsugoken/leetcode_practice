class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # can see ocean if all buildings to right are smaller
        #1>largest_seen
        #res = [3,2,0] -> res[::-1] = [0,2,3]
        # [4,2,3,1] largest_seen = 3
        #  ^
        largest_seen = float('-inf') 
        res = [] #$tores index of heights with ocean view
        for i in reversed(range(len(heights))):
            if heights[i]>largest_seen:
                res.append(i)
                largest_seen = heights[i]
        return res[::-1]
#TC: O(N)
#SC: O(N)