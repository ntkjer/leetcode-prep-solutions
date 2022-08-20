class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr_tank = 0
        total_tank = 0
        last_stop = 0
        
        for i, (g,c) in enumerate(zip(gas, cost)):
            
            curr_tank += g - c
            total_tank += g - c
            
            if curr_tank < 0:
                curr_tank = 0
                last_stop = i + 1
        
        return last_stop if total_tank >= 0 else -1
            