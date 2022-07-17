class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
            
        expected_sum = sum([i for i in range(len(nums) + 1)])
        return expected_sum - total