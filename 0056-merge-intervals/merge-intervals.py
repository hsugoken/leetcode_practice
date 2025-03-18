class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1) Are the intervals sorted? No
        # 2) How do we define overlapping intervals? # start_i+1 <= end_i
        # 3) Can there be duplicate intervals? Yes
        # 4) Do we modify input array or return a new one? 
        #Approach: Sort the intervals based on start_i and then check if overlaps and merge them
        intervals.sort(key= lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            if res and max(res[-1][0], intervals[i][0])<=min(res[-1][1], intervals[i][1]):
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res

        

        
