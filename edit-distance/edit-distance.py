class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(maxsize=None)
        def recur(i, j) -> int:
            if i == 0 or j == 0: return i or j
            
            if word1[i - 1] == word2[j - 1]:
                return recur(i - 1, j - 1)
            else:
                return 1 + min(recur(i - 1, j), recur(i, j - 1), recur(i - 1, j - 1))

        m, n = map(len, (word1, word2))
        # res = recur(m, n)
        # recur.cache_clear()

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]       
        
        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # we check left to insert
                    # we check upward to delete
                    # we check upper-left diag to replace both
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                      dp[i][j - 1],    
                                      dp[i - 1][j])

        return dp[-1][-1]