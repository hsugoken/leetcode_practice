# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #DO BFS and when we are at end of each level we add it to result
        if not root:
            return []
        queue = deque([root])
        #.           1<-
        #       2         3<-
        #.   5     4 <-
        # 6<-
        #
        #
        res = []
        #queue = []
        while queue:
            level_size = len(queue) #level_size=1
            for i in range(level_size): #i=0
                node = queue.popleft() #node=6
                if i==level_size-1:#0==0
                    res.append(node.val) #res = [1, 3,4, 6]
                
                if node.left:
                    queue.append(node.left) #
                if node.right:
                    queue.append(node.right)
        return res
#TC: O(N)
#SC: O(N)
        