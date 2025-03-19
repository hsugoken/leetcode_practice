"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.first = None
        self.last = None
        self.inorder_dfs(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first
    def inorder_dfs(self, node):
        if not node:
            return None
        self.inorder_dfs(node.left)
        if not self.last:
            self.first = node
        else:
            self.last.right = node
            node.left = self.last
        
        self.last = node

        self.inorder_dfs(node.right)

