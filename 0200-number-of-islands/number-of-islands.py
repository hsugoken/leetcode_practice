class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        count = 0

        def dfs(r,c):
            if 0<=r<M and 0<=c<N and grid[r][c]=="1":
                grid[r][c] = "0"
                nei = [[r+1,c], [r-1,c], [r,c+1],[r,c-1]]
                for nr,nc in nei:
                    dfs(nr,nc)
        
        for r in range(M):
            for c in range(N):
                if grid[r][c]=="1":
                    dfs(r,c)
                    count +=1
        
        return count
