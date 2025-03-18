class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #given each interval list is sorted and disjoint
        #intersection criteria? => max(start_i, start_j)<=min(end_i, end_j)
        def intersection(A,B):
            x = max(A[0],B[0])
            y = min(A[1],B[1])
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

