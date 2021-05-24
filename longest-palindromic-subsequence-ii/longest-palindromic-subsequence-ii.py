class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def recur(i, j, prev) -> int:
            """
            "Similar to LPS I, but we do not consider strings of len 1
            By the property of even nubmers, we only will have even results. 
            We also store the previously built palindrome and check if they are not same.
            """
            if i >= j:
                return 0
            if s[i] == s[j] and prev != s[i]:
                return 2 + recur(i + 1, j - 1)
            else:
                return min(recur(i + 1, j), recur(i, j - 1))

        # these early returns are speed-hacks
        if len(s) == 1:
            return 0
        elif len(s) == 2 and s[::-1]==s:
            return 2 
        
        # res = recur(0, len(s)-1)
        # recur.cache_clear()
        # similar to LPS, we tabulate s against itself to check palindromes formed
        # both from left to right and top to bottom

        # __________________
        #  | a | b | b | a |
        # a| 0 | 0 | 2 | 4 |
        # b|   | 0 | 2 |   |
        # b|   |   | 0 | 0 |
        # a|   |   |   | 0 |
        #  final solution state is in the upper right corner of our table
        #  we check our table for each substring length of 1, 2, 3... len(s)-1
        # we also check if we've previously already made this palindorm
        # since the question asks that bbbb != 4
        # so we store the palindrome created as a second field in the dp table
        
        dp = [[(0,"") for _ in range(len(s))] for _ in range(len(s))]
    
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1][1] != s[i]:
                    dp[i][j] = (2 + dp[i + 1][j - 1][0], s[i])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], key=lambda i:i[0])

        return dp[0][-1][0]
            
            
        