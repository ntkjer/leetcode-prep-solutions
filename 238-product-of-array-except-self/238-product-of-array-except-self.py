class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # left, right products
        # res[i] = left(i) * right(i)
        
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = list()
        
        n = len(nums) - 1
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(1, n + 1):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(n + 1):
            res.append(left[i] * right[i])
        
        return res