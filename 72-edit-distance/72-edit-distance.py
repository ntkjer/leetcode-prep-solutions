class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(i, j):
            if not i or not j:
                return i or j

            if word1[i - 1] == word2[j - 1]:
                return solve(i - 1, j - 1)
            else:
                return 1 + min(solve(i - 1, j), solve(i, j - 1), solve(i - 1, j - 1))
        
        res = solve(len(word1), len(word2))
        return res