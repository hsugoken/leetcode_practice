class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of number-> index
        #if target- current_number is in our tracked list return index, current_index
        track = {}
        for i, num in enumerate(nums):
            if (target-num) in track:
                return [track[target-num], i]
            track[num] = i
        return 