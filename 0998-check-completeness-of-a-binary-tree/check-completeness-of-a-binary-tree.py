# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        q = deque([root])
        null_seen = False
        #we basically go through the queue and then
        #check if it is a valdi node
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            #if null node is seen
            else:
                null_seen = True
                #we start a new BFS
                while q:
                    #we pop the remaininig elements in q
                    #and if it is not none then our BT is not complete
                    if q.popleft():
                        return False
        
        return True
