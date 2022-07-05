class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        l = 0
        res = []
        n = len(nums) - 1
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = n
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                        
                    l, r = l + 1, r - 1
                    
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
                    
        return res