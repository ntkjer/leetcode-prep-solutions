class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        res = list()
        candidates.sort()
        
        def backtrack(start, curr, partial=[]):
            if target == curr:
                res.append(partial[:])
            if curr >= target:
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                partial.append(candidates[i])
                backtrack(i + 1, curr + candidates[i], partial)
                partial.pop()
                prev = candidates[i]
                    
        backtrack(0, 0, [])
        return res