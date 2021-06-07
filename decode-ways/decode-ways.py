class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def solve(idx=0):
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

        res = solve()
        return res
            
            