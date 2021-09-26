class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recurrence    
        #   [1, 2, 3, 1] -> 4
        # T(0) = 0
        # T(i) = max(T(j) + nums[i], T(i)) if i >= 2
        # T(i) = nums[i] else
        N = len(nums) + 1
        result = [0] * N
        
        for i in range(1, len(nums) + 1):
            result[i] = nums[i - 1]
            if i >= 2:
                for j in range(i - 1):
                    result[i] = max(result[j] + nums[i - 1], result[i])

        return max(result)
        