class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #we will store the index and the number 
        #then we iterate through the list
        #if current number already exists in hashmap
        #then we check if the distance between the index value
        #is valid or not
        found = {} #num:index
        for i,num in enumerate(nums):
            if num in found and (i-found[num])<=k:
                return True
            found[num] = i
        return False

