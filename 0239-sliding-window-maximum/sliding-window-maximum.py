class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        queue = collections.deque()
        left = right = 0

        while right < len(nums):
            #pop smaller values than current number from the queue
            while queue and nums[queue[-1]]<nums[right]:
                queue.pop()
            
            queue.append(right)

            #if the left index is greater than the queue[0] means that element is out of bounds of queue
            if left > queue[0]:
                queue.popleft()
            
            if (right+1)>=k:
                output.append(nums[queue[0]])
                left+=1
            right +=1
        
        return output