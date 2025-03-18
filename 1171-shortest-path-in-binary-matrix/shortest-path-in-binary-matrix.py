class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #we will do a BFS and maintain a visited set
        N = len(grid)
        queue = deque([(0,0,1)]) #r,c,length
        visited =set((0,0))

        direct = [[1,0],[0,1],[-1,0],[0,-1],
                  [1,1],[-1,1],[-1,-1],[1,-1]]
        #[[0,1],
        # [1,0]]
        #r=0,c=0
        #visited = {(0,0)}
        #queue = [(0,0,1), (1,0,2), (0,1,2),(1,1,2)]
        while queue:
            r,c,dist = queue.popleft()
            #checks if
            if min(r,c)<0 or max(r,c)>=N or grid[r][c]:
                continue
            if r==N-1 and c==N-1:
                return dist
            
            for dr,dc in direct:
                if (r+dr, c+dc) not in visited:
                    queue.append((r+dr, c+dc, dist+1))
                    visited.add((r+dr, c+dc))

        return -1

#TC = O(N*N) #SC = O(N*N)
