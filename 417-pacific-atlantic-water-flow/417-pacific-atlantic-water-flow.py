class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[-1])
        
        def dfs(r, c, prev, visit):
            if (r,c) in visit or not (0 <= r < ROWS) or not(0 <= c < COLS) or prev > heights[r][c]:
                return False
            
            visit.add((r,c))
            curr = heights[r][c]    
            dfs(r + 1, c, curr, visit)
            dfs(r - 1, c, curr, visit)
            dfs(r, c + 1, curr, visit)
            dfs(r, c - 1, curr, visit)
            
            return True
        
        
        for r in range(ROWS):
            dfs(r, COLS - 1, heights[r][COLS - 1], pac)
            dfs(r, 0, heights[r][0], atl)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], atl)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], pac)
        
        return pac & atl
        
        
        