class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(find_left):
            l = 0
            r = len(nums)-1
            idx = -1
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid]<target:
                    l = mid + 1
                elif nums[mid]>target:
                    r = mid - 1
                else:
                    idx = mid
                    if find_left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx
        left_pos = binary_search(find_left=True)
        right_pos = binary_search(find_left=False)
        return [left_pos, right_pos]
