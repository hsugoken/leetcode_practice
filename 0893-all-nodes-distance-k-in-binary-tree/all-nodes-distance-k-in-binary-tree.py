# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #if k=0 then we return the target as it is at a distance 0 from itself
        if k==0:
            return [target.val]
        
        #we can do BFS to convert tree to form the graph
        #to form the graph we create the adjacency list
        graph = collections.defaultdict(set)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                #add the node to queue
                queue.append(node.left)
                #now build adjacency list
                graph[node].add(node.left)
                graph[node.left].add(node)
            if node.right:
                #add node to the queue
                queue.append(node.right)
                graph[node].add(node.right)
                graph[node.right].add(node)
        #now we have build the graph
        #now we will start BFS from there
        queue = collections.deque([(target, 0)])
        visited = set()
        res = []
        while queue:
            node, dist = queue.popleft()
            visited.add(node)
            if dist==k:
                res.append(node.val)
            for nei in graph[node]:
                if nei not in visited: 
                    queue.append((nei, dist+1))
        return res