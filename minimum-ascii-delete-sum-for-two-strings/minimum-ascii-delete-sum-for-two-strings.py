class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Top-down: Runtime @880ms,  38.77%
                  Memory  @33.5mb, 21.19%
        
        Bottom-up:  Runtime @ 564ms, 86.65%
                    Memory  @ 15.2mb, 73.94%
        """
        @lru_cache(maxsize=None) 
        def recur(i, j) -> int:
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return ord(s1[i]) + recur(i + 1, j + 1)
            else:
                return max(recur(i + 1, j), recur(i, j + 1))

        total_sum = sum(map(ord, (s1 + s2)))
        m, n = map(len, (s1, s2))
        
        #for c1, c2 in zip(s1, s2):
        #    total_sum += ord(c1) + ord(c2)
        # res = recur(0,0) 
        # recur.cache_clear()
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = ord(s1[i]) + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return total_sum - 2*dp[-1][-1]
            