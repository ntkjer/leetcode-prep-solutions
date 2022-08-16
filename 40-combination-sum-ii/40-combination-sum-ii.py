class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = list()
        
        def backtrack(start, partial, curr):
            if curr == target:
                res.append(partial[:])
            if curr >= target:
                return
            
            prev = None
            for i in range(start, len(candidates)):
                if prev and prev == candidates[i]:
                    continue
                    
                partial.append(candidates[i])
                backtrack(i + 1, partial, curr + candidates[i])
                partial.pop()
                prev = candidates[i]
        
        backtrack(0, [], 0)
        return res
            