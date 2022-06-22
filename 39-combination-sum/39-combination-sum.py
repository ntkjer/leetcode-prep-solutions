class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def solve(idx, curr, partial):
            if curr == target:
                res.append(partial[:])
                return
            if idx >= len(candidates) or curr > target:
                return
            
            partial.append(candidates[idx])
            solve(idx, curr + candidates[idx], partial)
            partial.pop()
            solve(idx + 1, curr, partial)
            return
        
        solve(0, 0, [])
        return res