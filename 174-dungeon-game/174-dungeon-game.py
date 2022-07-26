class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m, n = len(dungeon), len(dungeon[-1])
        
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        def valid_pos(x, y):
            if not(0 <= x < m) or not(0 <= y < n): 
                return False
            return True
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr = dungeon[i][j]
                
                if valid_pos(i + 1, j):
                    up = max(1, dp[i + 1][j] - curr)
                else:
                    up = float('inf')
                
                if valid_pos(i, j + 1):
                    left = max(1, dp[i][j + 1] - curr)
                else:
                    left = float('inf')
                
                next_health = min(up, left)
                if next_health != float('inf'):
                    dp[i][j] = next_health
                else:
                    if curr >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - curr
                        
        return dp[0][0]