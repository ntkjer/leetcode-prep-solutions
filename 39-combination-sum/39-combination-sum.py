class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        
        def solve(idx=0, partial=[], curr=0):
            if curr == target:
                res.append(partial[:])
                return
            
            if idx >= len(candidates) or curr > target:
                return
            
            partial.append(candidates[idx])
            solve(idx, partial, curr + candidates[idx])
            partial.pop()
            solve(idx + 1, partial, curr)
            return
        
        solve()
        return res