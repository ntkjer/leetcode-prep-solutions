class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def solve(idx=0):
            if idx == N:
                return 1
            if idx > N:
                return 0 
            if s[idx] == "0":
                return 0
            
            res = solve(idx + 1)
            pick_two = int(s[idx: idx + 2])
            if 10 <= pick_two <= 26:
                res += solve(idx + 2)

            return res
        
        N = len(s)
        #res = solve()
        #solve.cache_clear()
        #return res
        
        #dp = [0 for _ in range(N + 1)]
#
        #dp[0] = 1
        #dp[1] = 1 if s[0] != "0" else 0
        #
        #for i in range(2, len(dp)):
        #    if s[i - 1] != "0":
        #        dp[i] = dp[i - 1]
#
        #    pick_two = int(s[i - 2: i])
        #    if 10 <= pick_two <= 26:
        #        dp[i] += dp[i - 2]
        #    
        #return dp[N]

        prev_two, prev_one = 1, 1
        if s[0]  == "0":
            return 0

        for i in range(1, N):
            curr = 0
            if s[i] != "0":
                curr = prev_one

            pick_two = int(s[i - 1: i + 1])
            if 10 <= pick_two <= 26:
                curr += prev_two
            
            prev_two = prev_one
            prev_one = curr
        
        return prev_one
            
            