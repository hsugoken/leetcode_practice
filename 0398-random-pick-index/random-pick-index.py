#we are basically returning the index of the position where target exists
#in the number and doing so randomly or probabilistically
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hashmap = collections.defaultdict(list)
        for idx, val in enumerate(self.nums):
            #stores all the index for a particular value            
            self.hashmap[val].append(idx)


    def pick(self, target: int) -> int:
        return random.choice(self.hashmap[target])
        
# class Solution:

#     def __init__(self, nums: List[int]):
#         #nums => 1 2 3 3
#         #count=> 0 0 1 2
#         #random.randint(1,count)==count:pick_index=i
#         self.nums = nums

#     def pick(self, target: int) -> int:
#         count = 0
#         pick_index = 0
#         for i, num in enumerate(self.nums):
#             if num==target:
#                 count+=1
#                 if random.randint(1,count)==count:
#                     pick_index=i
        
#         return pick_index
        


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.pick(target)