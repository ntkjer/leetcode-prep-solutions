class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        starting_station = 0
        curr_tank = 0
        total_tank = 0
        
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1