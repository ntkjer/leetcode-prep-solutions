class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right, res = [0] * N, [0] * N, [0] * N

        left[0] = 1
        for i in range(1, N):
            left[i] = nums[i - 1] * left[i - 1]
        
        right[N - 1] = 1     
        for i in range(N - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(N):
            res[i] = left[i] * right[i]

        return res