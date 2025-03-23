class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        #Here we changed the nums to nums_set
        #this removes any duplicate element, might be needed for this problem
        for i in nums_set:
            cur_num = i #nums[i]

            if (cur_num-1) not in nums_set:
                cur_len = 1
                while cur_num+1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                max_len = max(cur_len, max_len)
        return max_len

