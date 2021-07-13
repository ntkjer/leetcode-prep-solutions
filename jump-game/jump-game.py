class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums) - 1 #last index we can jump to

        @cache 
        def solve(idx=0) -> bool:
            if idx == N:
                return True
            
            curr_jump = idx + nums[idx]
            
            for next_jump in range(idx + 1, curr_jump + 1):
                if solve(next_jump):
                    return True
                
            return False
        
        res = solve()
        return res