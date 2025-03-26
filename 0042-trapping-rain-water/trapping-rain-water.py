"""
# We cannot have any water stored on the end points
# We will move the pointer that has the smaller max value and shift
#Here at position i => (min(max_left, max_right)-h[i]) determines water trapping
#The minimum value will be the limiting factor
max_left => max height on left
max_right => max height on right


               *
[0,1,0,2,1,0,1,3,2,1,2,1]
               ^
water = 1+1+2+1+1
max_left = 2
max_right = 2
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = max_right = float('-inf')
        total_water = 0
        l, r = 0, len(height)-1
        while l<=r:
            #we focus on the pointer that is at a smaller height
            if height[l]<height[r]:
                max_left = max(height[l], max_left)
                total_water += (max_left-height[l])
                l += 1
            else:
                max_right = max(height[r], max_right)
                total_water += (max_right-height[r])
                r -= 1
        return total_water