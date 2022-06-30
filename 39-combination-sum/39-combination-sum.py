class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        
        def solve(idx, curr, partial):
            if idx == len(candidates): 
                return
            if curr == target:
                res.append(partial[:])
                return
            if curr >= target:
                return 
            
            partial.append(candidates[idx])
            solve(idx, curr + candidates[idx], partial)
            partial.pop()
            solve(idx + 1, curr, partial)
            
        
        solve(0, 0, [])
        return res