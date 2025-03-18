# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        def dfs(node):
            if not node:
                return 0
            if low<=node.val<=high:
                self.total += node.val
                dfs(node.left)
                dfs(node.right)
            if node.val<low:
                dfs(node.right)
            if node.val>high:
                dfs(node.left)
        dfs(root)
        return self.total