class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        while nums:
            curr = nums.pop()
            lo, hi = curr - 1, curr + 1
            
            while lo in nums:
                nums.remove(lo)
                lo -= 1
                
            while hi in nums:
                nums.remove(hi)
                hi += 1
                
            streak = max(streak, hi - lo - 1)
            
        return streak