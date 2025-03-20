class Solution:
    def isValid(self, s: str) -> bool:
        braces_map = {'(':')','{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in braces_map:
                stack.append(ch)
            else:
                if stack and braces_map[stack[-1]] == ch:
                        stack.pop()
                else:
                    return False
        return True if not stack else False