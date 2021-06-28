class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = N * [0]
        left = N * [0]
        right = N * [0]

        left[0] = 1
        for i in range(1, N):
            left[i] = nums[i - 1] * left[i - 1]
        
        R = 1
        for i in range(N - 1, -1, -1):
            R *= nums[i + 1] if i < N - 1 else 1
            result[i] = left[i] * R

        return result
        
        