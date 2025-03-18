class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[2,3,4,2,3,3,4] -> Sort: [2,2,3,3,3,4,4]
        #k=2                                 ^ ^
        #k is in the range of [1, number of unique elements in the array]
        #if array length is N. Then maximum value of number of unique elements
        #in the array would be N. ***
        #[_,_,_,_,_,_,_]
        #hashing => {count:[value]} #O(n) for hashmap construction
        #O(1) to get a value out
        #N=7=> [[0],[1],[2],[3],[4],[5],[6],[7]]
        #       [[],[],[2,4],[3],[],[],[],[]]
        #{2:[2,4],3:[3]}
        #nums: [2,3,4,2,3,3,4]
        #                   |
        countmap = {}
        for n in nums: #O(N)
            countmap[n] = countmap.get(n,0) + 1
            #{2:2, 3:3, 4:2}
            #           ^ |
        # buckets = [[]]*(len(nums)+1)
        ## Change this line: This creates multiple references to this same list

        buckets = [[] for _ in range(len(nums)+1)]
        print(buckets[0])
        #[[],[],[2,4],[3],[],[],[],[]]
        for number, count in countmap.items(): #O(N)
            # print(number, count)
            buckets[count].append(number)
            
        #[[],[],[2,4],[3],[],[],[],[]]
        #        ^
        # print(countmap, buckets)
        #res = [3,4]
        res = [] #k=2-1=1-1=0
        for i in reversed(range(len(buckets))):
            for j in buckets[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res
        

            
        