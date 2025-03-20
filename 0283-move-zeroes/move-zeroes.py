class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #move zeros to end or non-zeros to beginning
        l = 0
        #       L
        # 1,3,12,0,0
        #          ^
        #swap whenever we see a non-zero number
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
