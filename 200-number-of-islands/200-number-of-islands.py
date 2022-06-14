class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        ROWS, COLS = len(grid), len(grid[-1])
        count = 0
        WATER, LAND = "0", "1"
        
        
        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] is LAND:
                    dfs(x, y)
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] is LAND and (r,c) not in visited:
                    count += 1
                    dfs(r, c)
        
        return count