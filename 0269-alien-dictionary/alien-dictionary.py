class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #build adjacency list: for each character, store all characters 
        #that come after it this creates a graph where each character 
        #is a node and edges that represent ordering relationships
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        #compare adjacent words in the list tro determine character ordering
        for w1,w2, in zip(words,words[1:]):
            minLen = min(len(w1), len(w2))
            #invalid case: if w1 is longer than w2 and w1 is a prefix of w2
            #this violates the lexicographical rules
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            #find the first differing character and add an edge from w1[j] to w2[j]
            #this means that w1[j] comes before w2[j] in alien alphabet
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        #initialize data structure for topological sort
        visit = {} #False=visited, True=currently in path(cycle detection)
        res = [] #will store characters in reverse topological order
        #dfs search to detect cycles and build topological sort
        def dfs(c):
            #if charactyer is in current path, we have found a cycle
            if c in visit:
                return visit[c] 
            #mark as currently being visited (in current path)
            visit[c] = True
            #visit all the neighbors
            for nei in adj[c]:
                if dfs(nei):
                    return True # Propagate cycle detection
            #mark as fully visited and no longer in current path
            visit[c] = False
            #add to result (will be in reverse order)
            res.append(c)
            #non cycle found in tis path
            return False
        #try to perform topological sort on all characters
        for c in adj:
            if dfs(c):
                #cycle found , invalid alien dictionary
                return "" 
        #reverse to get correct topological order and joing into a string
        res.reverse()
        return "".join(res)
#so this visit basically is False for the terminal nodes and then we visit from another node to terminal
#we get back false so visit basically sets nodes as False for terminal nodes and then we move backwards like that

