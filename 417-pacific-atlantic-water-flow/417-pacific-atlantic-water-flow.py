class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        
        ROWS, COLS = len(heights), len(heights[-1])
        
        def dfs(r, c, prev, visit):
            if (r,c) in visit or not(0 <= r < ROWS) or not(0 <= c < COLS) or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            return
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], atl)
            dfs(r, COLS - 1, heights[r][COLS - 1], pac)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], atl)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], pac)
        
        return pac & atl
    
        