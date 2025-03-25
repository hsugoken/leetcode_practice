# import collections
# from collections import deque
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
        
#         neigbors = collections.defaultdict(list)
        
#         wordList.append(beginWord)
#         #created the adjacencey list pattern -> [words]
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j]+"*"+word[j+1:]
#                 neigbors[pattern].append(word)
        
#         q = deque([beginWord])
#         res = 1
#         visited = set([beginWord])

#         while q:

#             #iterate through each level
#             for i in range(len(q)):
#                 currword = q.popleft()

#                 if currword == endWord:
#                     return res
                
#                 #this adds the next nodes to visit in the queue
#                 for j in range(len(currword)):
#                     pattern = currword[:j] + "*" + currword[j+1:]
#                     for neiWord in neigbors[pattern]:
#                         if neiWord not in visited:
#                             q.append(neiWord)
#                             visited.add(neiWord)
#             res += 1
        
#         return 0
                    

         
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Return 0 if endWord is not in wordList since we can't reach it
        if endWord not in wordList:
            return 0

        # Create adjacency list using defaultdict to store pattern -> word mappings 
        nei = collections.defaultdict(list)
        wordList.append(beginWord)  # Add beginWord to wordList for pattern matching

        # Build patterns for each word
        # For "hit" we create: "*it", "h*t", "hi*"
        # This helps us find words that differ by one letter
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # Initialize BFS with starting word
        visit = set([beginWord])    # Track visited words to avoid cycles
        q = deque([beginWord])      # Queue for BFS traversal
        res = 1                     # Length of transformation sequence (start word counts as 1)
        
        # BFS to find shortest path
        while q:
            # Process all words at current level
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:  # Found the target word
                    return res
                
                #once we check a node above, we are checking the neighbors and adding to queue

                # Try changing each letter position
                for j in range(len(word)):
                    # Create pattern for current position
                    pattern = word[:j] + "*" + word[j+1:]
                    # Check all words matching this pattern
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:  # Only process unvisited words
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1  # Increment path length after processing entire level
        
        return 0  # Return 0 if no transformation sequence found