"""
1) keep hash_map to update the location of an index
2) when we iterate through the array, 
    a) if nums[i] in hash_map we check if it satisfies abs(i-j)<=k: return True
    b) else previous index is of no use so we just remove it and update
    the current index
3) return False if we reach end

https://leetcode.com/problems/contains-duplicate-ii/solutions/6012642/video-2-solutions-hashmap-set
"""

# indices: [0,1,2,3,4,5]
# nums:    [1,2,3,1,2,3] k=2
#                     ^
# hash_map = {1:0, 2:1,3:2} (4-1)<=2 F


# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         hash_map = {}
#         for i in range(len(nums)):
#             if nums[i] in hash_map and (i-hash_map[nums[i]])<=k:
#                     return True
#             hash_map[nums[i]] = i
#         return False
#TC: O(n)
#SC: O(min(n,k))
"""
The space complexity can be better analyzed as O(min(n,k)) rather than O(n), since the hash map will contain at most min(n,k) entries. This happens because once we've seen more than k elements, older entries beyond the k-element window become irrelevant.
"""


"""
# Sliding window
i - k - 1

i: current position
k: search range from current position
-1: next position of edge of target range

1) remove the element at start of window once i>k
    window.remove(nums[i-k-1])
2) if curren number is already in window return True
3) now add current number to window

"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window =set()
        for i in range(len(nums)):
            #remove element outside the window of size k
            if i>k:
                window.remove(nums[i-k-1])
            #check if current element is in window
            if nums[i] in window:
                return True
            #add current element to window
            window.add(nums[i])
        return False
#TC: O(N)            
#SC: O(min(N,k))



