class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 0, -1):
            res += nums[i] - nums[0]
            
        return res