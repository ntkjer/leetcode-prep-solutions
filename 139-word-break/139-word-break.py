class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1, len(dp)):
            for j in range(i):
                if s[j: i] in words and dp[j]:
                    dp[i] = True
        
        return dp[-1]