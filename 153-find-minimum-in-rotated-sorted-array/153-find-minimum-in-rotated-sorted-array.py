class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotation idx?
        
        lo, hi = 0, len(nums) - 1
        res = float('inf')
        while lo < hi:
            mid = (lo + hi) // 2
            # normal array
            res = min(nums[lo], res)
            
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
            
        return nums[lo]