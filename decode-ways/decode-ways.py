class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def solve(idx=0) -> int:
            if idx == len(s):
                return 1
            if s[idx] == "0":
                return 0
            if idx == len(s) - 1:
                return 1
            
            res = solve(idx + 1)
            pick_two = int(s[idx: idx + 2])
            if pick_two >= 10 and pick_two <= 26:
                res += solve(idx + 2)
            return res

        #res = solve()
        #solve.cache_clear()
        
        # we fill up our dp table to tabulate as we go:
        #     3  2  6
        # [0, 1, 1, 2]
        #        x 

        # we dont add at x mark becase 32 is out of bounds.
        
        #     2  2  6
        # [0, 1, 2, 3]

        # 0 ways to make ""
        # 1 way to make first char
        # add the rest until len(s) + 1 (final state)

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1 # it takes 
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            pick_two = int(s[i - 2: i])
            if pick_two >= 10 and pick_two <= 26:
                dp[i] += dp[i - 2]

        res = dp[-1]
        return res
