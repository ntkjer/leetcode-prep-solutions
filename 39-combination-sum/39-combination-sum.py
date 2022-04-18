class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(idx, partial, curr):
            if curr == target:
                res.append(partial[:])
                return
            
            if idx == len(candidates) or curr > target:
                return
            
            partial.append(candidates[idx])
            solve(idx, partial, curr + candidates[idx])
            partial.pop()
            solve(idx + 1, partial, curr)
        
        solve(0, [], 0)
        return res