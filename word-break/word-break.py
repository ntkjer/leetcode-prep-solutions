class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #(1.)
        #words = set(wordDict) 
        #@cache 
        #def backtrack(s, start):
        #    if start == len(s):
        #        return True
        #    for end in range(start + 1, len(s) + 1):
        #        if s[start:end] in words and backtrack(s, end):
        #            return True
        #    return False
        #
        #res = backtrack(s, 0)
        
        #(2.)
        #if not s:
        #    return False
        #visited = set()
        #words = set(wordDict)
        #q = collections.deque()
        #q.append(0)
        #N = len(s)

        #while q:
        #    start = q.popleft()
        #    if start in visited:
        #        continue
        #    for end in range(start + 1, N + 1):
        #        if s[start:end] in words:
        #            q.append(end)
        #        if end == N:
        #            return True
        #        visited.add(start)

        #return False
        
        # (3.)
        # s can be divided into subproblems s1 and s2
        # if s1 and s2 satisfies conditions of problem P
        # then s must also satisfy P
        # i.e catsanddog -> catsand, dog
        #.                  cats, and, dog
        
        N = len(s)
        dp = [False] * (N + 1)
        words = set(wordDict)
        
        dp[0] = True # empty string is always present in D
        # for every substring partition string into further substring s1' and s2' using idx j
        
        for i in range(1, N + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
        
        
        
            
            
            
       
            
            