class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        res = 0
        
        visit = set()
        rows, cols = len(grid), len(grid[-1])
        WATER, LAND = "0", "1"
        
        def dfs(r, c):
            if (r,c) in visit:
                return
            if not (0 <= r < rows) or not (0 <= c < cols):
                return
            if grid[r][c] == WATER:
                return
            
            visit.add((r,c))
            for dx, dy in directions:
                dfs(dx + r, dy + c)
            
            return 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND and (r,c) not in visit:
                    res += 1
                    dfs(r, c)
        return res
                    