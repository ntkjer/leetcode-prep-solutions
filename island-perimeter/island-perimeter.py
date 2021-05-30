class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        WATER = 0
        LAND = 1
        M, N = len(grid), len(grid[-1])

        perimeter = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == LAND:
                    if r == 0 or grid[r - 1][c] is WATER:
                        perimeter += 1
                    if c == 0 or grid[r][c - 1] is WATER:
                        perimeter += 1
                    if r == M - 1 or grid[r + 1][c] is WATER:
                        perimeter += 1
                    if c == N - 1 or grid[r][c + 1] is WATER:
                        perimeter += 1                        

        return perimeter
            
            
            
            
        
        
        