class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[-1])
        
        pac, atl = set(), set()
        directions = ((1,0), (0,1), (-1,0), (0, -1))
        
        def dfs(x, y, visited, prev):
            if (x,y) in visited or not(0 <= x < R) or not(0 <= y < C) or heights[x][y] < prev:
                return
            
            visited.add((x,y))
            for dx,dy in directions:
                dfs(x + dx, y + dy, visited, heights[x][y])
        
        for r in range(R):
            dfs(r, 0, atl, heights[r][0])
            dfs(r, C - 1, pac, heights[r][C - 1])
        
        for c in range(C):
            dfs(0, c, atl, heights[0][c])
            dfs(R - 1, c, pac, heights[R - 1][c])
        
        return pac & atl