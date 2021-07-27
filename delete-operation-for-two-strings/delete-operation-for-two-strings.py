class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        
        Tn = O(|m| * |n|)
        Sn = O(|m| * |n|)
            
            
        Bottom up solution that utilizes the levehnstein distance algo:
         initial table values correspond to the edit distance of each string 
         let word1, word2 = eat, sea
          _________________
          | s | e | a |   |
         e| 0 | 1 | 2 | 3 |
         a| 1 | 0 | 1 |2  |
         t| 2 | 1 | 2 |2  |
          | 3 |   |   |2  |

         bottom right diagonal represents correct final state (2).
         if the words match, we add 0 and the current i,j state is i-1,j-1 
         this is the upper left diagonal of the current value
         if they dont match we look up and left and add one to the minimum value.
         
        Another way to solve this is to find the LCS between two strings and return m + n - 2*LCS
        However solving it via the edit distance for two strings is the preferable strat.
        
        Top-down recurisive solution provided for convenience.
        """
        @cache 
        def solve(i, j) -> int:
            if i == 0 or j == 0:
                return i or j
            if word1[i - 1] == word2[j - 1]:
                return solve(i - 1, j - 1)
            else:
                return 1 + min(solve(i - 1, j), solve(i, j - 1))

        m, n = map(len, (word1, word2))
        #res = solve(m, n)
        
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
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
        