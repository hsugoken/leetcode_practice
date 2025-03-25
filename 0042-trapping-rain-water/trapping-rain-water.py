class Solution:
    def trap(self, height: List[int]) -> int:
        #               R
        #[0,1,0,2,1,0,1,3]
        #             L
        maxL = float('-inf') #maxL=2
        maxR = float('-inf') #maxR=3
        water = 0#5 ex
        left, right = 0, len(height)-1 #0,7
        while left<right:
            if height[left]<height[right]:#0<3
                maxL = max(height[left], maxL)#2
                water += maxL-height[left] #2-0=2
                left += 1
            else:
                maxR = max(height[right], maxR)
                water += maxR-height[right]
                right -= 1
        return water
