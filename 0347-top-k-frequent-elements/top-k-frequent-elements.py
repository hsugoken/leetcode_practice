class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we will count the frequency for each number then
        #create bins for that frequency: [[0],[1], [2], ..., [N]]
        #and we pop from the end till k>=0
        freq_count = {}
        for n in nums:
            freq_count[n] = freq_count.get(n, 0) + 1
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in freq_count.items():
            buckets[freq].append(num)
        
        for i in reversed(range(len(buckets))):
            for j in buckets[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res
        

#TC: O(N)
#SC: O(N)
        


