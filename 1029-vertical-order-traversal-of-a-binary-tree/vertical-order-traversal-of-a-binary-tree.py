# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
                1(0,0)
       2(1,-1)           4(1,1) 
          5(2,0)   3(2,0)    6(2,2)

#output: [[1], [2, 4], [3,5,6]]
"""

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = deque([(root, 0,0)]) #node, r, c
        colmap = collections.defaultdict(list) #col -> node val
        min_col = float('inf') #-1
        max_col = float('-inf') #2
        #colmap = {0:[(0,1),(2,5),(2,3)], -1:[(1,2)],1:[(1,4)], 2:[(2,6)]} c:(r,val)
        #queue = []
        while queue:
            node, row, col = queue.popleft() #(6,2,2)
            colmap[col].append((row, node.val))
            min_col = min(col, min_col)
            max_col = max(col, max_col)

            if node.left:
                queue.append((node.left, row+1, col-1))

            if node.right:
                queue.append((node.right, row+1, col+1))
        #colmap = {0:[(0,1),(2,5),(2,3)], -1:[(1,2)],1:[(1,4)], 2:[(2,6)]} 
        #min_col = -1
        #max_col= 2
        #c in [-1,0,1,2]
        for c in range(min_col, max_col+1):
            sorted_vals = sorted(colmap[c], key=lambda x: (x[0], x[1]))
            #[(0,1),(2,3),(2,5)]
            res.append([i[1] for i in sorted_vals])
        #res = [[2],[1,3,5],[4],[6]]
        return res