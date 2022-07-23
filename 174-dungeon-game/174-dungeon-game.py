class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[-1])
        dp = [float('inf') for _ in range(n + 1)]
        dp[n - 1] = 1
        # max(1, (min(dp[j], dp[j + 1]) - dungeon[i][j]));
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = max(1, (min(dp[j], dp[j + 1])) - dungeon[i][j])
                
        return dp[0]