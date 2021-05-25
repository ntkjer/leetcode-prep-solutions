class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        
        # solves the same exact way as the LPS pattern
        # this only considers strings that are different
        # for abc
        # 12, 01, 02
        # bc, ab, ac 
        # we add counts for diags which are one len c, so 1 + 1 + 1 for abc
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            count += dp[i][i]
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and ((j - i) < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    count += dp[i][j]
            
        # an alternate way of solving the problem is to check for all strings as we loop
        # so this will yield for abc
        # i  j
        # 2  2
        # 1  1
        # 0  0
        # 0  1 
        # 0  2
        # this gives convenience of only maintaining one invariant in loop
       # 
       # for i in range(len(s) - 1, -1, -1):
       #     for j in range(i, len(s)):
       #         if s[i] == s[j] and ((j - i + 1) < 3 or dp[i + 1][j - 1]):
       #             dp[i][j] = 1
       #             count += dp[i][j]
       #         
        return count
        
        
                
       