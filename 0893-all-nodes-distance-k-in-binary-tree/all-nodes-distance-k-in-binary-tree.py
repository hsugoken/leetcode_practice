# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
             return [target.val]
        
        q = deque([root])
        graph = collections.defaultdict(set)

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                graph[node].add(node.left)
                graph[node.left].add(node)
            if node.right:
                q.append(node.right)
                graph[node].add(node.right)
                graph[node.right].add(node)
        #now we will do bfs from target node
        q = deque([(target, 0)])
        res = []
        visit = set()
        while q:
            node, dist = q.popleft()
            visit.add(node)
            if dist==k:
                res.append(node.val)
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append((nei, dist+1))
        return res

