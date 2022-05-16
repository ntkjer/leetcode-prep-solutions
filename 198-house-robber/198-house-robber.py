class Solution:
    def rob(self, nums: List[int]) -> int:
        
        first, second = 0, 0
        for n in nums:
            curr = max(first + n, second)
            first = second
            second = max(curr, second)
        return second