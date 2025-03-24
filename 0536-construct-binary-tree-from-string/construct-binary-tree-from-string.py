# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        #check if we are given a string
        if not s:
            return None
        stack = []
        #need to iterate over our string from left to right
        i = 0
        while i < len(s):
            cur_char = s[i]
            if cur_char == '-':
                #parse all the digits from next character
                i+=1
                val=0
                while i < len(s) and s[i].isdigit():
                    val = val*10 + int(s[i])
                    i += 1
                #at the end of our loop we will incremement it so decrement here
                i -= 1 
                stack.append(TreeNode(-val))
            elif cur_char.isdigit():
                val = 0 
                while i < len(s) and s[i].isdigit():
                    val = val*10 + int(s[i])
                    i += 1
                i -= 1
                stack.append(TreeNode(val))
            elif cur_char == ")":
                top = stack.pop()
                if not stack[-1].left:
                    stack[-1].left = top
                else:
                    stack[-1].right = top
            i += 1
        return stack[-1]