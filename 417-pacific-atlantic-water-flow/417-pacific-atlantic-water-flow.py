class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac, atl = set(), set()
        M, N = len(heights), len(heights[0])
        
        def dfs(x, y, visited, prev):
            if (x,y) in visited or (not(0 <= x < M) or 
                                    not(0 <= y < N) or 
                                    heights[x][y] < prev):
                return
            visited.add((x,y))
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])
                
                
        for r in range(M):
            dfs(r, 0, atl, heights[r][0])
            dfs(r, N - 1, pac, heights[r][N - 1])
        
        for c in range(N):
            dfs(0, c, atl, heights[0][c])
            dfs(M - 1, c, pac, heights[M - 1][c])
        
        return pac & atl