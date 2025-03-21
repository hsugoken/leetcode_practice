class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i,ch in enumerate(s):
            if stack and ch==stack[-1]:
                stack.pop()
                continue
            stack.append(ch)
        return ''.join(stack)