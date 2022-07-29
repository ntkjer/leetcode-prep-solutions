class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        
        def backtrack(i, curr, partial):
            if curr == target:
                res.append(partial[:])
            if curr >= target or i >= len(candidates):
                return 
            
            partial.append(candidates[i])
            backtrack(i, candidates[i] + curr, partial)
            partial.pop()
            backtrack(i + 1, curr, partial)
            
        backtrack(0, 0, [])
        return res