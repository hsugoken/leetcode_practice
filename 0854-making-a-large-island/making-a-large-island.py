class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        size = collections.defaultdict(int)
        label = 2
        def out_of_bounds(r,c):
            return min(r,c)<0 or max(r,c)>=N
        
        def dfs(r,c,label):
            if out_of_bounds(r,c) or grid[r][c]!=1:
                return 0
            grid[r][c] = label
            island_size = 1
            nei = [[r+1,c],[r,c-1],[r-1,c],[r,c+1]]
            for nr, nc in nei:
                island_size += dfs(nr, nc, label)                
            return island_size
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    size[label] = dfs(r,c,label)
                    label += 1

        #max_size = 0 if not size else max(size.values())
        max_size = max(size.values()) if size else 0

        def check_flip(r,c):
            area = 1
            visit = set()
            nei = [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]
            for nr,nc in nei:
                if not out_of_bounds(nr,nc) and grid[nr][nc]>1: #and grid[nr][nc] not in visit:
                    cur_label = grid[nr][nc]
                    if cur_label not in visit:
                        visit.add(cur_label)
                        area += size[cur_label]
            return area

        for r in range(N):
            for c in range(N):
                if grid[r][c]==0:
                    max_size = max(max_size, check_flip(r,c))
        
        return max_size