# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.total = 0
        self.dfs(root, 0)
        return self.total
    def dfs(self, node, cur_sum):
        cur_sum = cur_sum*10 + node.val

        if not node.left and not node.right:
            self.total += cur_sum

        if node.left:
            self.dfs(node.left, cur_sum)

        if node.right:
            self.dfs(node.right, cur_sum)


        
