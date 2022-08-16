class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[-1])
        
        def is_valid_pos(r, c):
            if not (0 <= r < m) or not(0 <= c < n): 
                return False
            return True
        
        
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                up = float('inf')
                left = float('inf')
                
                curr = dungeon[i][j]
                
                if is_valid_pos(i + 1, j):
                    up = max(dp[i + 1][j] - curr, 1)
                if is_valid_pos(i, j + 1):
                    left = max(dp[i][j + 1] - curr, 1)
                
                
                candidate = min(up, left)
                if candidate != float('inf'):
                    dp[i][j] = candidate
                else:
                    if curr >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - curr
        
        return dp[0][0]