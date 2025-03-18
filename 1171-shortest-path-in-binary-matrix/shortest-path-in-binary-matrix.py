class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        R = len(grid)
        C = len(grid[0])
        N = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1],
                      [1,1],[-1,-1],[-1,1],[1,-1]]

        visit = set()
        q = deque([(0,0,1)])
        #def bfs(q):
        visit.add((0,0))
        while q:
            r,c,dist = q.popleft()
            if (r<0 or r>=R) or (c<0 or c>=C) or (grid[r][c]==1):
                continue
            if r == N-1 and c == N-1:
                return dist
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (nr,nc) not in visit:
                    visit.add((nr,nc))
                    q.append([nr,nc,dist+1])
        return -1