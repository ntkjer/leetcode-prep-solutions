class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def solve(nums):
            first, second = 0, 0
            for num in nums:
                curr = max(num + first, second)
                first = second
                second = max(curr, second)
                
            return second
        
        return max(solve(nums[1:]), solve(nums[:-1]), nums[0])