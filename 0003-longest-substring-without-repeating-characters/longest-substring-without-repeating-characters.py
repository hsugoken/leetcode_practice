class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Key Idea:
        # Use sliding window with two pointers (l and r).
        # Move right pointer to expand window, and left pointer to shrink window
        # whenever a duplicate character is encountered.

        max_len = 0                  # Stores the length of the longest substring found
        cur_window = set()          # Stores characters in the current window (no duplicates)
        l = 0                       # Left pointer of the sliding window

        for r in range(len(s)):     # Right pointer expands the window
            # If s[r] is a duplicate, shrink window from the left
            while s[r] in cur_window:
                cur_window.remove(s[l])
                l += 1
            # Add current character and update max length
            cur_window.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len

# Edge Cases:
# 1. Empty string → return 0
# 2. All unique characters → return len(s)
# 3. All duplicates (e.g., "aaaa") → return 1

# Time Complexity: O(N)
# - Each character is added and removed from the set at most once

# Space Complexity: O(min(N, M))
# - Set stores at most M unique characters (M = charset size, e.g. 26 or 128)
