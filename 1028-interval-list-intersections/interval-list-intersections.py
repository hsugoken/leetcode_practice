#Edge cases:
#If either list is empty, the while loop condition will fail
#Zero-length intervals (where start=end) are handled correctly by the intersection logic; the max/min comparison still works for these cases.
#The condition firstList[p1][1] <= secondList[p2][1] is used to decide which pointer to increment based on which interval ends first. This is clever because:
#If interval A ends before or at the same time as interval B, we've found all possible intersections with A, so we should move to the next interval in the first list.
#Otherwise, interval B ends first, so we've found all possible intersections with B and should move to the next interval in the second list.
#Zero Length intervals are also handled well by this [5,5], [3,5]
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #given each interval list is sorted and disjoint
        #intersection criteria? => max(start_i, start_j)<=min(end_i, end_j)
        def intersection(A,B):
            x = max(A[0],B[0]) #Get the latest start point
            y = min(A[1],B[1]) #Get the earliest end point
            if x<=y:
                return [x, y]
            return False
        p1 = p2 = 0
        res = []
        while p1<len(firstList) and p2<len(secondList):
            temp = intersection(firstList[p1], secondList[p2])
            if temp:
                res.append(temp)
            #end_i<=end_j
            if firstList[p1][1]<=secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return res

#TC: O(N) N = total length (L1+L2) where L1 and L2 are the lengths for the lists
#SC: O(N) 