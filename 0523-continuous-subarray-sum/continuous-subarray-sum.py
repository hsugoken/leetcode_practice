class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0:-1}
        total = 0
        #23,2,4,6,7
        #hash_map = {0:-1,5:0,1:1}
        for i,num in enumerate(nums):
            total += num #29
            rem = total%k #29%6=5
            if rem in hash_map:
                if (i-hash_map[rem])>=2:
                    return True
            else:
                hash_map[rem] = i
        return False
            

        