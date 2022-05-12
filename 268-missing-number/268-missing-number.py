class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected_sums = [i for i in range(N + 1)]
       
        curr_sums = 0
        for n in nums:
            curr_sums += n
        
        return sum(expected_sums) - curr_sums