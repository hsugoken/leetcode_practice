class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0]**2+x[1]**2
        heap = []
        for p in points[:k]:
            heap.append([-dist(p),p[0],p[1]])
        heapq.heapify(heap)
        for p in points[k:]:
            cur_dist = -dist(p)
            if heap[0][0]<cur_dist:
                heapq.heappushpop(heap, [cur_dist, p[0],p[1]])
        # print(heap)
        return [[x[1],x[2]] for x in heap]