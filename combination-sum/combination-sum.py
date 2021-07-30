class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        result = list()
        
        def solve(remaining=target, partial=[], i=0):
            if remaining < 0:
                return 
            
            elif remaining == 0:
                result.append(list(partial))
                return
            
            for j in range(i, N):
                partial.append(candidates[j])
                solve(remaining - candidates[j], partial, j)
                partial.pop()
            
        solve()
        return result
                
                
                    
            
            
            