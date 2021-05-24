class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]: #speed-hacks for LC submission time.
            return len(s)
        if len(s) == 1: 
            return 1
        
        @lru_cache(maxsize=None)
        def solve(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return 2 + solve(i + 1, j - 1)
            else:
                return max(solve(i + 1, j), solve(i, j - 1))

        #res = solve(0, len(s) - 1)
        #solve.cache_clear()
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # we populate our table as writing the string same forwards and backwards
        #   c a t
        # c 1   *
        # a   1
        # t     1
         
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1 #all strings of len 1 are at the diagonal of the matrix
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][-1] #upper right diag represented by * as target
        
            