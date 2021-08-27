class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        result = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    result[i] = max(1 + result[j], result[i])

        max_idx = 0
        for i in range(n):
            if result[i] > result[max_idx]:
                max_idx = i
                
        return result[max_idx]
            
    