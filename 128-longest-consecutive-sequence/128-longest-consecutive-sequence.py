class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        streak = 0
        
        while nums:
            curr_streak = 1
            curr = nums.pop()
            lo, hi = curr - 1, curr + 1
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