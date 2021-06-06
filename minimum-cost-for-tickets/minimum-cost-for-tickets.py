class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)  
        N = len(days)
        durations = [1, 7, 30]
        
        @lru_cache(None)
        def solve(i=1):
            """
            dp(i)= min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
            """
            if i > 365:
                return 0

            elif i in dayset:
                res = float('inf')
                for c, d in zip(costs, durations):
                    res = min(res, solve(i + d) + c)
                return res
            else:
                return solve(i + 1)


        @lru_cache(None)
        def solve_2(i=0):
            if i >= N:
                return 0
            res = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                res = min(res, solve_2(j) + c)
            return res

        longest_duration = days[-1]        
        dp = [0 for i in range(longest_duration + 1)]
        for i in range(longest_duration + 1):
            if i not in dayset:
                dp[i] = dp[i - 1]
            else:
                # check per day, week, and month values
                # uses max(0, i - D) to indicate strictly increasing i for i..D where D is nth day to consider
                dp[i] = min(dp[max(0, i - 7)] + costs[1],
                           dp[max(0, i - 1)] + costs[0],
                           dp[max(0, i - 30)] + costs[2])
        return dp[-1]
                    