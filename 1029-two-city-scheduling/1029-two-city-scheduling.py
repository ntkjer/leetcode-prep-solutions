class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda i: i[0] - i[1])
        
        total_cost = 0
        
        n = len(costs) // 2
        
        i = 0
        
        while i < n:
            total_cost += costs[i][0] + costs[i + n][1]
            i += 1
        
        return total_cost