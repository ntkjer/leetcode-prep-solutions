class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[-1])
        
        def dfs(r, c):
            if (r, c) in visit:
                return
            if not(0 <= r < rows) or not(0 <= c < cols) or grid[r][c] == "0":
                return
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return
        
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands