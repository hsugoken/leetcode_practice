"""
[10,2,3,4,11,9,5,6]
9,10,11 
2,3,4,5,6 
idnetify start of longest sequence
{10,2,3,4,11,9,5,6}
             ^
9 is start [10,11,] 3<5
2 is the start [3,4,5,6]
longest = 5  
cur_num-1 should not be there  

{10,2,3,4,11,9,5,6}
                 ^
cur_num = 2,2+1,3+1,4+1,5+1
cur_len = 1, 2,  3,  4,  5

cur_num = 11
cur_len = 3

longest = max(cur_len, longest) = 5 #5>3

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = set(nums)
        longest = 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                cur_num = n
                cur_len = 1
                #2,cur_len= 4
                #3,4,5
                while (cur_num + 1) in nums:
                    cur_num += 1
                    cur_len += 1
                longest = max(cur_len, longest)
        return longest

        