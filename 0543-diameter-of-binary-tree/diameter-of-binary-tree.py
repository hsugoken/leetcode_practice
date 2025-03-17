# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longestPath(node):
            nonlocal diameter
            if not node:
                return 0
            left = longestPath(node.left)
            right = longestPath(node.right)
            diameter = max(left+right, diameter)
            return 1 + max(left, right)
        longestPath(root)
        return diameter
            