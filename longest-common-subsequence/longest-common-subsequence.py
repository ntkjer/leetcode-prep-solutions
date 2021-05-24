class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Two implementations:
            - top-down recursize with memoization.
            - bottom-up dp solution
        Both solutions are Tn = O(|m| * |n|) where m and n are lengths of inputs.
        Space complexity is linear for both but bottom up leaves room for further optimization.
        We can achive further optimal results by just keeping track of previous two sol states.
        """
        @lru_cache(maxsize=None) 
        def solve_recur(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)
            else:
                return max(solve(i + 1, j), solve(i, j + 1))

        #res = solve(0,0)
        #solve.cache_clear()
        m, n = map(len, (text1, text2)) 
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # here we are filling our dp table s.t. the bottom right diagonal will contain 
        # the most optimal solution state
        # as we traverse the dag of solution states, we select the most optimal state
        # which exploits the optimal substructure of dp problems. 
        # this is the same as a topological sort of the DAG substates, and guarantees the most 
        # optimal solution s.t. a greedy solution does not exist.
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]