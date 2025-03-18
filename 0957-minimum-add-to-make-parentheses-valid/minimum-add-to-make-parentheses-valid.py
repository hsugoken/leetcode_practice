class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        closed_count = 0
        for ch in s:
            if ch=="(":
                open_count += 1
            elif ch==")":
                if open_count:
                    open_count -= 1
                else:
                    closed_count += 1
        return open_count+closed_count