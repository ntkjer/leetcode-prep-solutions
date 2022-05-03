class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def isValid(x, y, prev):
            if (0 <= x < ROWS and 0 <= y < COLS and prev <= heights[x][y]):
                return True
            return False
        
        def dfs(x, y, prev, visited):
            if (x,y) in visited or not isValid(x, y, prev):
                return
            
            visited.add((x, y))
            curr = heights[x][y]
            dfs(x + 1, y, curr, visited)
            dfs(x, y + 1, curr, visited)
            dfs(x - 1, y, curr, visited)
            dfs(x, y - 1, curr, visited)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], atl)
            dfs(r, COLS - 1, heights[r][COLS - 1], pac)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], atl)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], pac)
        
        return pac & atl