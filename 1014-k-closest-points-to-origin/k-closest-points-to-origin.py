class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0]**2+x[1]**2
        nums = [[dist(point), point[0], point[1]] for point in points]
        def quickselect(left, right):
            # Base case
            if left >= right:
                return
            pivot = nums[right][0]
            pidx = left
            for i in range(left, right):
                if nums[i][0]<=pivot:
                    nums[i], nums[pidx] = nums[pidx], nums[i]
                    pidx += 1
            nums[pidx], nums[right] = nums[right], nums[pidx]
            if pidx > k-1: 
                quickselect(left, pidx-1)
            elif pidx < k-1: 
                quickselect(pidx+1, right)
            # If pidx == k-1, we're done
        
        # Run quickselect
        quickselect(0, len(nums)-1) 
        # Return the k closest points
        return [[nums[i][1], nums[i][2]] for i in range(k)]
        # def dist(x):
        #     return x[0]**2+x[1]**2
        # #compute the distances and take -ve of squared distance
        # #add it to heap (max-heap)
        # heap = [(-dist(point), point[0], point[1]) for point in points[:k]]
        # heapq.heapify(heap)
        # for point in points[k:]:
        #     cur_dist = -dist(point)
        #     if cur_dist>heap[0][0]:
        #         heapq.heappushpop(heap, (cur_dist, point[0],point[1]))
        # res = [[x[1],x[2]] for x in heap]
        # return res