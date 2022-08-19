class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[-1])
        
        def is_valid(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols):
                return False
            return True
        
        def dfs(r, c):
            if (r,c) in visit:
                return
            visit.add((r,c))
            
            if grid[r][c] != "1":
                return
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = dx + r, dy + c
                if not is_valid(x, y):
                    continue
                dfs(x, y)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands