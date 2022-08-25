class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[-1])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        def isValidRow(r, c):
            if not (0 <= r < m) or not(0 <= c < n):
                return False
            return True
        
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # check right, if we are in bounds
                # check up, if we are in bound
                curr = dungeon[i][j]
                
                if isValidRow(i + 1, j):
                    up = max(dp[i + 1][j] - curr, 1)
                else:
                    up = float('inf')
                
                if isValidRow(i, j + 1):
                    right = max(dp[i][j + 1] - curr, 1)
                else:
                    right = float('inf')
                
                
                candidate = min(up, right)
                
                if candidate != float('inf'):
                    dp[i][j] = candidate
                else:
                    if curr >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - curr
                
        
        
        return dp[0][0]