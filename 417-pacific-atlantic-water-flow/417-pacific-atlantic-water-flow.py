class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[-1])
        
        pac = set()
        atl = set()
        
        def dfs(r, c, prev, visit):
            if (r,c) in visit: 
                return
            
            if not(0 <= r < rows) or not(0 <= c < cols):
                return 
            
            if heights[r][c] < prev:
                return
            
            visit.add((r,c))
            curr = heights[r][c]
            dfs(r + 1, c, curr, visit)
            dfs(r, c + 1, curr, visit)
            dfs(r, c - 1, curr, visit)
            dfs(r - 1, c, curr, visit)
            
        for r in range(rows):
            dfs(r, 0, heights[r][0], atl)
            dfs(r, cols - 1, heights[r][cols - 1], pac)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], atl)
            dfs(rows - 1, c, heights[rows - 1][c], pac)
            
        return pac & atl