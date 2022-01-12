class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache 
        def solve(steps: int) -> int:
            if steps == 0:
                return 1     
            if steps == 1:
                return 1

            return solve(steps - 2) + solve(steps - 1)
        
        return solve(n)