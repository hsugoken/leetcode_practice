# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

      1
  3        2*
4   5    6*    7*
     8*
dfs(1) -> 3+2=5
dfs(3) -> 2+1
dfs(4)->1
dfs(5) -> 2
dfs(8)-> 1
dfs(2)-> 2
dfs(6) -> 1
dfs(7) -> 1





"""
#calculate diameter at each node
#calculate longest path
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 #3
        def dfs(node):
            if not node:
                return 0
            #node at 3
            left_path = dfs(node.left) #1
            right_path = dfs(node.right) #2
            self.diameter = max(self.diameter, left_path+right_path)
            return max(left_path,right_path) + 1
        dfs(root)
        return self.diameter

#TC: O(N)
#SC: O(log N) / O(N)
        