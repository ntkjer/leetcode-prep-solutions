class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dfs?
        
        words = set(wordDict)
        visited = set() 
        N = len(s)  

        @cache 
        def dfs(start=0):
            if start == N:
                return True
            for end in range(start + 1, N + 1):
                if s[start:end] in words and dfs(end):
                    return True
            return False
         
        return dfs()
         
           