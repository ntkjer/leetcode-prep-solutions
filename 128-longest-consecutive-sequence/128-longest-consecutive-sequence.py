class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        while nums:
            num = nums.pop()
            curr_streak = 1
            lo, hi = num - 1, num + 1
            while nums and hi in nums:
                curr_streak += 1
                nums.remove(hi)
                hi += 1
                
            while nums and lo in nums:
                curr_streak += 1
                nums.remove(lo)
                lo -= 1
            
            streak = max(streak, curr_streak)
        
        return streak
                