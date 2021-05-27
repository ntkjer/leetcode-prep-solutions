class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # climb one or two steps
        # 
    
        @lru_cache(maxsize=None)
        def recur(step):
            if step <= 1:
                return 0

            take_one = cost[step - 1] + recur(step - 1)
            take_two = cost[step - 2] + recur(step - 2) 

            return min(take_one, take_two)

 #        dp = [0 for _ in range(len(cost) + 1)] 
 #        for i in range(2, len(cost) + 1):   
 #            one_step = cost[i - 1] + dp[i - 1]
 #            two_step = cost[i - 2] + dp[i - 2]
 #            
 #            dp[i] = min(one_step, two_step)
        
        prev_one, prev_two = 0, 0
        res = 0
        for i in range(2, len(cost) + 1):
            temp = prev_one
            prev_one = min(prev_one + cost[i - 1], prev_two + cost[i - 2])
            prev_two = temp 
#       prev_one represents min-cost to reach the top-floor since
#       we consider the top floor a step.
        return prev_one 
            
