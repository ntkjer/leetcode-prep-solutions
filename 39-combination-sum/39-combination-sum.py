class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        
        def backtrack(idx, curr, partial=[]):
            if curr > target or idx >= len(candidates):
                return
            if curr == target:
                res.append(partial[:])
                return
            partial.append(candidates[idx])
            backtrack(idx, curr + candidates[idx], partial)
            partial.pop()
            backtrack(idx + 1, curr, partial)
        
        backtrack(0, 0, [])
        return res