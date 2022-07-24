class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # max can be the product of two numbers
        # need to keep track of global max, curent_max, and negative_max?
        
        cur_max = nums[0]
        res = nums[0]
        cur_min = nums[0]
        
        for num in nums[1:]:
            tmp = max(num, cur_max * num, cur_min * num) 
            cur_min = min(num, cur_min * num, cur_max * num)
            cur_max = tmp
            res = max(res, tmp)
        
        
        #           [-2, 0, -1]
        # cur_max = -2, 0, 2
        # res     = -2, 0
        # cur_min = -2, -2
        return res