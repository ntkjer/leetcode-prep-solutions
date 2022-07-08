class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[-1])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev):
            if ((r,c) in visit or not(0 <= r < rows) or 
                not(0 <= c < cols) or prev > heights[r][c]):
                return
            visit.add((r,c))
            
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            return
        
        for r in range(rows):
            dfs(r, 0, atl, heights[r][0])
            dfs(r, cols - 1, pac, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, atl, heights[0][c])
            dfs(rows - 1, c, pac, heights[rows - 1][c])
            
        return pac & atl