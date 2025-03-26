"""
1) We're working with a perfect binary tree (all internal nodes have two children and all leaves are at the same level)
2) "Is the tree guaranteed to be a perfect binary tree, or could it be incomplete?"
"""
#https://claude.ai/chat/d6028f38-16d6-4cef-95b6-840e0f633f8c
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        cur = root
        nxt = root.left if root.left else None
    
        while cur and nxt:
            #connect cur left and cur right 
            cur.left.next = cur.right
            #connecting the left and right nodes next
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next

            if not cur:
                cur = nxt
                nxt = cur.left
        return root
            
        