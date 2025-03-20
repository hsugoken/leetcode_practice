# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not target:
            return 0
        cur = root
        closest = root.val
        while cur:
            if target==cur.val:
                return cur.val
            if abs(closest-target)>abs(cur.val-target):
                closest = cur.val
            elif abs(closest-target)==abs(cur.val-target):
                closest = min(closest, cur.val)
            
            if target<cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return closest