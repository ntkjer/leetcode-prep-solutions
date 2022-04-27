class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[-1])
        atl, pac = set(), set()
        
        def dfs(r,c, visited, prev):
            if (r, c) in visited or not(0 <= r < M) or not(0 <= c < N) or heights[r][c] < prev:
                return 
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            
        for c in range(N):
            dfs(0, c, pac, heights[0][c])
            dfs(M - 1, c, atl, heights[M - 1][c])
        
        
        for r in range(M):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, N - 1, atl, heights[r][N - 1])
            

            
        return atl & pac