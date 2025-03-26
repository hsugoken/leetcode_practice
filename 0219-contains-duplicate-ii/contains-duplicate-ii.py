"""
1) keep hash_map to update the location of an index
2) when we iterate through the array, 
    a) if nums[i] in hash_map we check if it satisfies abs(i-j)<=k: return True
    b) else previous index is of no use so we just remove it and update
    the current index
3) return False if we reach end

"""

# indices: [0,1,2,3,4,5]
# nums:    [1,2,3,1,2,3] k=2
#                     ^
# hash_map = {1:0, 2:1,3:2} (4-1)<=2 F


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map and (i-hash_map[nums[i]])<=k:
                    return True
            hash_map[nums[i]] = i
        return False