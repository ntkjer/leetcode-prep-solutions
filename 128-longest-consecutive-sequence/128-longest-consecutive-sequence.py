class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        
        lo, hi = 0, 0
        streak = 1
        while nums:
            num = nums.pop()
            lo = num - 1
            hi = num + 1
            curr_streak = 1
            while lo in nums:
                curr_streak += 1
                nums.remove(lo)
                lo -= 1
                
            while hi in nums:
                curr_streak += 1
                nums.remove(hi)
                hi += 1
            
            streak = max(streak, curr_streak)
        return streak
                
            
        