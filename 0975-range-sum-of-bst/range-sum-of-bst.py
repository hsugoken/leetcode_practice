# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         self.total = 0
#         def dfs(node):
#             if not node:
#                 return 0
#             if low<=node.val<=high:
#                 self.total += node.val
#                 dfs(node.left)
#                 dfs(node.right)
#             if node.val<low:
#                 dfs(node.right)
#             if node.val>high:
#                 dfs(node.left)
#         dfs(root)
#         return self.total

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val<low:
                stack.append(curr.right)
            if curr.val>high:
                stack.append(curr.left)
            if low<=curr.val<=high:
                stack.append(curr.left)
                stack.append(curr.right)
                total += curr.val
        return total


#TC: O(N)
#SC: O(N)