class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        
        rows, cols = len(dungeon), len(dungeon[-1])
        
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        def valid_pos(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols):
                return False
            return True
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                
                curr_cell = dungeon[i][j]
                
                
                if valid_pos(i + 1, j):
                    up = max(dp[i + 1][j] - curr_cell, 1)  
                else:
                    up = float('inf')
                
                if valid_pos(i, j + 1):
                    down = max(dp[i][j + 1] - curr_cell, 1)
                else:
                    down = float('inf')
                
                candidate = min(up, down)
                if candidate != float('inf'):
                    dp[i][j] = candidate
                else:
                    if curr_cell >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - curr_cell
                        
        
        return dp[0][0]