class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        max_seen = "0"
        max_i = -1
        swap_i = swap_j = -1 
        ##swap_i index of number to be swapped on left with index of number to be swapped on right
        for i in reversed(range(len(nums))):
            if nums[i]>max_seen:
                max_seen = nums[i]
                max_i = i
            elif nums[i]<max_seen:
                swap_i = i
                swap_j = max_i
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]
        return int(''.join(nums))

